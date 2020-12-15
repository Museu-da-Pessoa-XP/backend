from django.test import TestCase
from setuptools.command.test import test

from museu.models import Historia, User
from museu.tests.utils import *


class ModelsTestCase(TestCase):

    def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        self.user = None

    def setUp(self):
        string_length = random.randint(1, 24)
        num_historias = random.randint(10, 20)

        # Historia parameters
        self.name, self.email, self.phone = create_users_data(num_historias, string_length)
        self.historia_titles, self.historia_tags, self.historia_types, self.historia_media_url \
            = create_historias_data(num_historias, string_length)

        for name, email, phone, title, htags, htype, media_url in zip(
                self.name, self.email, self.phone,
                self.historia_titles, self.historia_tags,
                self.historia_types, self.historia_media_url):
            user = User.objects.create(name=name, email=email, phone=phone)
            historia = Historia.objects.create(user=user, title=title, type=htype, media_url=media_url)
            historia.tags.add(*save_tags(htags))

    def test_historia_model(self):
        historias_created = Historia.objects.all().order_by('title').distinct('title')

        historias = []

        for name, email, phone, title, htags, htype, media_url in zip(
                self.name, self.email, self.phone,
                self.historia_titles, self.historia_tags,
                self.historia_types, self.historia_media_url):
            user = User.objects.create(name=name, email=email, phone=phone)
            historia = Historia.objects.create(user=user, title=title, type=htype, media_url=media_url)
            historia.tags.add(*save_tags(htags))
            historias.append(historia)

        historias.sort(key=lambda x: x.title)

        for i in range(len(historias)):
            self.assertEqual(historias[i].user.name, historias_created[i].user.name)
            self.assertEqual(historias[i].user.email, historias_created[i].user.email)
            self.assertEqual(historias[i].user.phone, historias_created[i].user.phone)
            self.assertEqual(historias[i].title, historias_created[i].title)
            self.assertEqual(list(historias[i].tags.values_list('tag')),
                             list(historias_created[i].tags.values_list('tag')))
            self.assertEqual(historias[i].type, historias_created[i].type)
            self.assertEqual(historias[i].media_url, historias_created[i].media_url)



    def test_user_model(self):
        users_created = User.objects.all().order_by('name').distinct('name')
        users = []

        for name, email, phone in zip(self.name, self.email, self.phone):
            usr = User.objects.create(name=name, email=email, phone=phone)
            users.append(usr)

        users = sorted(users, key=lambda x: x.name)

        for i in range(len(users)):
            self.assertEqual(users[i].name, users_created[i].name)
            self.assertEqual(users[i].email, users_created[i].email)
            self.assertEqual(users[i].phone, users_created[i].phone)
