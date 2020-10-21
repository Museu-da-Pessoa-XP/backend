import random
import string

from django.test import TestCase
from .models import User, USER_MAX_LENGTH


def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


class UserTestCase(TestCase):

    def setUp(self):
        string_length = random.randint(1, USER_MAX_LENGTH)
        num_string = random.randint(10, 20)
        email_suffix = "@email.com"
        self.user_names = [get_random_string(string_length) for i in range(num_string)]
        self.emails = [user_name+email_suffix for user_name in self.user_names]
        for user_name, email in zip(self.user_names, self.emails):
            User.objects.create(name=user_name, email=email)

    def test_user_model(self):
        users = []
        for user_name, email in zip(self.user_names, self.emails):
            users.append(User.objects.create(name=user_name, email=email))
        for i in range(len(users)):
            self.assertEqual(users[i].name, self.user_names[i])
            self.assertEqual(users[i].email, self.emails[i])
