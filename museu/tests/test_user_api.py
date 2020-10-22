
import json
import random
import string
import requests

from django.test import TestCase
from rest_framework.test import APIRequestFactory

from museu.views import UserView


def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


class UserAPITestCase(TestCase):

    def setUp(self):
        self.users = []
        email_suffix = '@email.com'
        num_users = random.randint(10, 20)
        for i in range(num_users):
            self.users.append({
                "data": {
                    "name": get_random_string(random.randint(10, 20)),
                    "email": get_random_string(random.randint(5, 10)) + email_suffix
                }
            })

    def test_get(self):
        factory = APIRequestFactory()
        u = UserView()
        for user in self.users:
            r = factory.post('/user/', user, format='json')
            u = UserView()
            _ = u.post(r)
        users = json.loads(u.get('').content)
        for user_from_get, user_inserted in zip(users, self.users):
            user_inserted = user_inserted['data']
            self.assertEqual(user_from_get['name'], user_inserted['name'])
            self.assertEqual(user_from_get['email'], user_inserted['email'])

    def test_post(self):
        factory = APIRequestFactory()
        for user in self.users:
            r = factory.post('/user/', user, format='json')
            u = UserView()
            res = u.post(r)
            self.assertEqual(res.status_code, requests.status_codes.codes.created)
