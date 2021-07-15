import json
from django.core.signing import dumps
from graphql_relay import to_global_id
from graphene_django.utils.testing import GraphQLTestCase
from unittest import skip

from schema import schema
from users.tests import const
from users.models import User, ShippingInfo


class UserQueryTestCase(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema
    fixtures = ['fixtures/users.json']

    def test_user_query(self):
        response = self.query(
            const.GET_USER_QUERY,
            op_name='user',
            variables={"id": to_global_id('UserNode', '2')},
        )
        content = json.loads(response.content)['data']
        user = User.objects.get(pk=2)
        self.assertResponseNoErrors(response)
        self.assertEqual(content['user']['email'], user.email)
        shipping_info = content['user']['shippinginfoSet']['edges']
        self.assertEqual(len(shipping_info), user.shippinginfo_set.count())

    def test_all_users_query(self):
        response = self.query(
            const.GET_USERS_QUERY,
            op_name='allUsers',
            variables={'email': 'user', 'isStaff': False, 'isActive': True}
        )
        content = json.loads(response.content)['data']['allUsers']
        users = User.objects.filter(email__icontains='user', is_staff=False, is_active=True)
        self.assertResponseNoErrors(response)
        self.assertEqual(len(content['edges']), users.count())

    def test_create_user(self):
        response = self.query(
            const.CREATE_USER_MUTATION,
            op_name='createUser',
            input_data={
                'email': 'new@email.com',
                'password': 'test123123'
            }
        )
        content = json.loads(response.content)['data']['createUser']['user']
        new_user = User.objects.get(email='new@email.com')
        self.assertResponseNoErrors(response)
        self.assertEqual(content['email'], new_user.email)
        self.assertFalse(content['isActive'])
        self.assertFalse(new_user.is_active)

    def test_activate_user(self):
        user = User.objects.get(pk=6)
        token = dumps(user.pk)
        response = self.query(
            const.ACTIVATE_USER_MUTATION,
            op_name='activateUser',
            input_data={'token': token}
        )
        content = json.loads(response.content)['data']['activateUser']['user']
        user.refresh_from_db()
        self.assertResponseNoErrors(response)
        self.assertTrue(content['isActive'])
        self.assertTrue(user.is_active)

    def test_change_user_password(self):
        response = self.query(
            const.CHANGE_USER_PASSWORD_MUTATION,
            op_name='changeUserPassword',
            input_data={
                'gid': to_global_id('UserNode', '5'),
                'password': 'another123123',
            }
        )
        self.assertResponseNoErrors(response)
        self.assertTrue(User.objects.get(pk=5).check_password('another123123'))

    @skip('Enable after added authentication')
    def test_deactivate_user(self):
        response = self.query(
            const.DEACTIVATE_USER_MUTATION,
            op_name='deactivateUser',
            input_data={
                'gid': to_global_id('UserNode', '7'),
            },
        )
        content = json.loads(response.content)['data']['deactivateUser']['user']
        self.assertResponseNoErrors(response)
        self.assertFalse(content['isActive'])
        self.assertFalse(User.objects.get(pk=7).is_active)

    @skip('Enable after added authentication')
    def test_delete_user(self):
        response = self.query(
            const.DELETE_USER_MUTATION,
            op_name='deleteUser',
            input_data={
                'gid': to_global_id('UserNode', '8'),
            },
        )
        content = json.loads(response.content)
        self.assertResponseNoErrors(response)
        self.assertTrue(content['ok'])
