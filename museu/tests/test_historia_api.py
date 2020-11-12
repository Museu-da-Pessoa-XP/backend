
import json
import random
from io import BytesIO

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from museu.views import HistoriaView
from museu.tests.utils import create_historias_data

TEST_PATH = 'tests/'


class HistoriaAPITestCase(TestCase):

	def setUp(self):
		self.historias = []
		num_historias = random.randint(10, 20)

		file = BytesIO(b'Test File content')
		file.seek(0)

		titles, descriptions, types, media_urls = create_historias_data(num_historias)
		for title, description, htype, media in zip(titles, descriptions, types, media_urls):
			self.historias.append({
				"title": title,
				"description": description,
				"type": htype,
				"media": file
			})

	def test_get(self):
		api_client = APIClient()
		hv = HistoriaView()
		for historia in self.historias:
			api_client.post('/historia/', data=historia, format='multipart')

		historias = json.loads(hv.get('').content)
		for hist_from_get, hist_inserted in zip(historias, self.historias):
			self.assertEqual(hist_from_get['title'], hist_inserted['title'])
			self.assertEqual(hist_from_get['description'], hist_inserted['description'])
			self.assertEqual(hist_from_get['type'], hist_inserted['type'])
			# self.assertEqual(hist_from_get['media'], hist_inserted['media_url'])

	def test_post(self):
		api_client = APIClient()
		for historia in self.historias:
			response = api_client.post('/historia/', data=historia, format='multipart')
			self.assertEqual(status.is_success(response.status_code), True)
