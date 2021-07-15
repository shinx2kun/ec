import graphene
from django.conf import settings
from graphene import relay, ObjectType
from graphql import GraphQLError
from django.db import transaction
from django.template.loader import render_to_string
from django.core.signing import dumps, loads, SignatureExpired, BadSignature
from graphql_relay import from_global_id

from users.models import User
from users.schema import UserNode
from backend.models import ShoppingCart


class AlreadyExistUser(Exception):
    pass


class AlreadyActiveUser(Exception):
    pass


class NotPermitted(Exception):
    pass


class CreateUser(relay.ClientIDMutation):
    class Input:
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    user = graphene.Field(UserNode)

    @classmethod
    @transaction.atomic
    def mutate_and_get_payload(cls, root, info, email, password):
        try:
            normalized_email = User.objects.normalize_email(email)
            user, is_created = User.objects.get_or_create(email=normalized_email)
            subject = f"【{settings.SHOP_NAME}】仮登録完了と本登録のお願い"
            context = {
                'link': f"{settings.FRONTEND_URL}register/?id={dumps(user.pk)}",
                'shop_name': settings.SHOP_NAME,
                'info_email': settings.INFO_EMAIL,
                'info_tel': settings.INFO_TEL,
            }
            message = render_to_string('users/user_register.html', context)
            if not is_created:
                if not user.is_active:
                    # Send email again for not activated user
                    user.set_password(password)
                    user.save()
                    user.email_user(
                        subject=subject,
                        body=message,
                        html=True
                    )
                    return CreateUser(user=user)
                else:
                    raise AlreadyExistUser
            user.set_password(password)
            user.is_active = False
            user.save()
            user.email_user(
                subject=subject,
                body=message,
                html=True
            )
            #ユーザー作成時に、ユーザーに紐づくショッピングカートを作成
            user_shopping_cart = ShoppingCart()
            user_shopping_cart.user = user
            user_shopping_cart.save()
        except AlreadyExistUser:
            raise GraphQLError(f"{email}は既に登録されています。")
        except Exception as e:
            raise GraphQLError(f"Errorが発生しました: {e}")

        return CreateUser(user=user)


class ActivateUser(relay.ClientIDMutation):
    class Input:
        token = graphene.String(required=True)

    user = graphene.Field(UserNode)

    @classmethod
    @transaction.atomic
    def mutate_and_get_payload(cls, root, info, token):
        try:
            timeout_sec = getattr(settings, 'ACTIVATION_TIMEOUT_SEC', 60*60*24)
            user_pk = loads(token, max_age=timeout_sec)
            user = User.objects.get(pk=user_pk)
            subject = f"【{settings.SHOP_NAME}】本登録完了のお知らせ"
            context = {
                'shop_name': settings.SHOP_NAME,
                'info_email': settings.INFO_EMAIL,
                'info_tel': settings.INFO_TEL,
            }
            message = render_to_string('users/user_activated.html', context)
            if not user.is_active:
                user.is_active = True
                user.is_superuser = False
                user.is_staff = False
                user.save()
                user.email_user(
                    subject=subject,
                    body=message,
                    html=True
                )
            else:
                raise AlreadyActiveUser
        except SignatureExpired:
            raise GraphQLError(
                "URLが期限切れのため本登録が完了できませんでした。再度仮登録を実施し本登録メールの再発行を行ってください。"
            )
        except BadSignature:
            raise GraphQLError(
                "認証情報に誤りがあるため本登録が完了できませんでした。メールに記載されたURLとブラウザに入力されたURLが同一であることを確認してください。"
            )
        except User.DoesNotExist:
            raise GraphQLError(
                f"ユーザ情報が取得できませんでした。{settings.INFO_EMAIL}までお問い合わせください。"
            )
        except AlreadyActiveUser:
            raise GraphQLError("既に本登録が完了しています。")
        except Exception as e:
            raise GraphQLError(f"Errorが発生しました: {e}")

        return CreateUser(user=user)


class ChangeUserPassword(relay.ClientIDMutation):
    class Input:
        gid = graphene.ID()
        password = graphene.String(required=True)

    user = graphene.Field(UserNode)

    @classmethod
    @transaction.atomic
    def mutate_and_get_payload(cls, root, info, gid, password):
        try:
            user = User.objects.get(pk=from_global_id(gid)[1])
            user.set_password(password)
            user.save()
        except User.DoesNotExist:
            raise GraphQLError(
                f"ユーザ情報が取得できませんでした。{settings.INFO_EMAIL}までお問い合わせください。"
            )
        except Exception as e:
            raise GraphQLError(f"Errorが発生しました: {e}")

        return CreateUser(user=user)


class DeactivateUser(relay.ClientIDMutation):
    class Input:
        gid = graphene.ID()

    user = graphene.Field(UserNode)

    @classmethod
    @transaction.atomic
    def mutate_and_get_payload(cls, root, info, gid):
        try:
            if not info.context.user.is_superuser:
                raise NotPermitted
            user = User.objects.get(pk=from_global_id(gid)[1])
            user.is_active = False
            user.save()
        except NotPermitted:
            raise GraphQLError("権限がありません。")
        except User.DoesNotExist:
            raise GraphQLError(f"ユーザ情報が取得できませんでした。")
        except Exception as e:
            raise GraphQLError(f"Errorが発生しました: {e}")

        return CreateUser(user=user)


class DeleteUser(relay.ClientIDMutation):
    class Input:
        gid = graphene.ID()

    ok = graphene.Boolean()

    @classmethod
    @transaction.atomic
    def mutate_and_get_payload(cls, root, info, gid):
        try:
            if not info.context.user.is_superuser:
                raise NotPermitted
            user = User.objects.get(pk=from_global_id(gid)[1])
            user.delete()
        except NotPermitted:
            raise GraphQLError("権限がありません。")
        except User.DoesNotExist:
            raise GraphQLError(f"ユーザ情報が取得できませんでした。")
        except Exception as e:
            raise GraphQLError(f"Errorが発生しました: {e}")

        return cls(ok=True)


class UsersMutation(ObjectType):
    create_user = CreateUser.Field()
    activate_user = ActivateUser.Field()
    change_user_password = ChangeUserPassword.Field()
    deactivate_user = DeactivateUser.Field()
    delete_user = DeleteUser.Field()