
import random
import string

from django.test import TestCase
from museu.models import User, Historia, USER_MAX_LENGTH


def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


class ModelsTestCase(TestCase):

    def setUp(self):
        string_length = random.randint(1, USER_MAX_LENGTH)
        num_string = random.randint(10, 20)
        email_suffix = "@email.com"
        self.user_names = [get_random_string(string_length) for i in range(num_string)]
        self.emails = [user_name+email_suffix for user_name in self.user_names]
        self.historia_names = [get_random_string(string_length) for i in range(num_string)]
        self.locations = [get_random_string(string_length) for i in range(num_string)]
        self.users = []
        for username, email, historia_name, location in zip(self.user_names, self.emails,
                                                            self.historia_names, self.locations):
            User.objects.create(name=username, email=email)
            user = User.objects.get(name=username)
            self.users.append(user)
            Historia.objects.create(name=historia_name, location=location, user=user)

    def test_user_model(self):
        users_created = User.objects.all()
        users = []
        for user_name, email in zip(self.user_names, self.emails):
            users.append(User.objects.create(name=user_name, email=email))
        for i in range(len(users)):
            self.assertEqual(users[i].name, users_created[i].name)
            self.assertEqual(users[i].email, users_created[i].email)

    def test_historia_model(self):
        historias_created = Historia.objects.all()
        historias = []
        for historia_name, location, user in zip(self.historia_names, self.locations, self.users):
            historias.append(Historia.objects.create(name=historia_name, location=location, user=user))
        for i in range(len(historias)):
            self.assertEqual(historias[i].name, historias_created[i].name)
            self.assertEqual(historias[i].location, historias_created[i].location)
            self.assertEqual(historias[i].user, historias_created[i].user)
