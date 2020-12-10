
import json
import random
from io import BytesIO

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from museu.views import AppView
from museu.tests.utils import *


class HistoriaAPITestCase(TestCase):

    def setUp(self):
        self.historias = []
        num_historias = random.randint(10, 20)

        name, email, phone = create_users_data(num_historias)
        titles, tags, types, media = create_historias_data(num_historias, is_model=False)
        for title, htags, htype, media, name, email, phone in zip(titles, tags, types, media, name, email, phone):
            self.historias.append({
                'name': name,
                'email': email,
                'phone': phone,
                'title': title,
                'tags': htags,
                'type': htype,
                'media': media,
            })


    def test_get(self):
        api_client = APIClient()
        view = AppView()
        for historia in self.historias:
            api_client.post('/historia/', data=historia, format='multipart')

        historias = json.loads(view.get('').content)

        # TODO: missing assertEqual on tags, media and User
        for hist_from_get, hist_inserted in zip(historias, self.historias):
            self.assertEqual(hist_from_get['title'], hist_inserted['title'])
            self.assertEqual(hist_from_get['type'], hist_inserted['type'])

    def test_post(self):
        api_client = APIClient()
        for historia in self.historias:
            response = api_client.post('/historia/', data=historia, format='multipart')
            self.assertEqual(status.is_success(response.status_code), True)
