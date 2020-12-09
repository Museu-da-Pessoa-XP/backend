
import random

from django.test import TestCase
from museu.models import Historia
from museu.tests.utils import create_historias_data


class ModelsTestCase(TestCase):

    def setUp(self):
        string_length = random.randint(1, 30)
        num_historias = random.randint(10, 20)

        # Historia parameters
        self.historia_titles, self.historia_descriptions, self.historia_types, self.historia_media_url \
            = create_historias_data(num_historias, string_length)

        for title, description, htype, media_url in zip(self.historia_titles, self.historia_descriptions,
                                                        self.historia_types, self.historia_media_url):
            Historia.objects.create(title=title, description=description, type=htype, media_url=media_url)

    def test_historia_model(self):
        historias_created = Historia.objects.all()
        historias = []

        for title, description, htype, media_url in zip(self.historia_titles, self.historia_descriptions,
                                                        self.historia_types, self.historia_media_url):
            historias.append(Historia.objects.create(title=title, description=description,
                                                     type=htype, media_url=media_url))

        for i in range(len(historias)):
            self.assertEqual(historias[i].title, historias_created[i].title)
            self.assertEqual(historias[i].description, historias_created[i].description)
            self.assertEqual(historias[i].type, historias_created[i].type)
            self.assertEqual(historias[i].media_url, historias_created[i].media_url)
