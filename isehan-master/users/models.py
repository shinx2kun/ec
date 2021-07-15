from django.db import models
from django.contrib.auth import models as auth_models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from utils import create_email


class MyUserManager(auth_models.BaseUserManager):
    """ユーザーマネージャー."""
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """メールアドレスでの登録を必須にする"""
        if not email:
            raise ValueError('The given email must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """is_staff(管理サイトにログインできるか)と、is_superuer(全ての権限)をFalseに"""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """スーパーユーザーは、is_staffとis_superuserをTrueに"""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)


class User(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    class Meta:
        verbose_name = 'ユーザ'
        verbose_name_plural = 'ユーザ'

    """カスタムユーザーモデル."""
    email = models.EmailField('メールアドレス', max_length=150, null=False, blank=False, unique=True)
    is_staff = models.BooleanField(
        '管理者',
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        '有効',
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = MyUserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def email_user(self, subject, body, from_email=None, html=False):
        """Send an email to this user."""
        email = create_email(
            subject=subject,
            body=body,
            from_email=from_email,
            to=[self.email],
            html=html
        )

        email.send()

    @property
    def username(self):
        """username属性のゲッター
        他アプリケーションが、username属性にアクセスした場合に備えて定義
        メールアドレスを返す
        """
        return self.email


class ShippingInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField('宛名', max_length=150)
    zipcode = models.CharField('郵便番号', max_length=8)
    address1 = models.CharField('都道府県', max_length=20)
    address2 = models.CharField('市区町村番地', max_length=500)
    address3 = models.CharField('建物名', max_length=500)

    def __str__(self):
        return self.name
