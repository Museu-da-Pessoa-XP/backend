
from django.test import TestCase
from setuptools.command.test import test

from museu.models import Historia, User
from museu.tests.utils import *


class ModelsTestCase(TestCase):

    def setUp(self):
        string_length = random.randint(1, 30)
        num_historias = random.randint(10, 20)

        # Historia parameters
        self.historia_titles, self.historia_tags, self.historia_types, self.historia_media_url \
            = create_historias_data(num_historias, string_length)

        self.name, self.email, self.phone = create_users_data(num_historias, string_length)

        for title, htags, htype, media_url in zip(self.historia_titles, self.historia_tags,
                                                  self.historia_types, self.historia_media_url):
            hist = Historia.objects.create(title=title, type=htype, media_url=media_url)
            hist.tags.add(*save_tags(htags))

        for name, email, phone in zip(self.name, self.email, self.phone):
            User.objects.create(name=name, email=email, phone=phone)


    def test_historia_model(self):
        historias_created = Historia.objects.all()
        historias = []

        for title, htags, htype, media_url in zip(self.historia_titles, self.historia_tags,
                                                        self.historia_types, self.historia_media_url):
            hist = Historia.objects.create(title=title,type=htype, media_url=media_url)
            hist.tags.add(*save_tags(htags))
            historias.append(hist)

        for i in range(len(historias)):
            self.assertEqual(historias[i].title, historias_created[i].title)
            self.assertEqual(list(historias[i].tags.values_list('tag')),
                             list(historias_created[i].tags.values_list('tag')))
            self.assertEqual(historias[i].type, historias_created[i].type)
            self.assertEqual(historias[i].media_url, historias_created[i].media_url)

    def test_user_model(self):
        users_created = User.objects.all()
        users = []

        for name, email, phone in zip(self.name, self.email, self.phone):
            usr = User.objects.create(name=name,email=email, phone=phone)
            users.append(usr)

        for i in range(len(users)):
            self.assertEqual(users[i].name, users_created[i].name)
            self.assertEqual(users[i].email, users_created[i].email)
            self.assertEqual(users[i].phone, users_created[i].phone)
