
import json
import random
import string
import requests

from django.test import TestCase
from rest_framework.test import APIRequestFactory

from museu.views import HistoriaView, UserView


def get_random_string(length):
	letters = string.ascii_lowercase
	result_str = ''.join(random.choice(letters) for i in range(length))
	return result_str


class HistoriaAPITestCase(TestCase):

	def setUp(self):
		self.historias = []
		email_suffix = '@email.com'

		user_factory = APIRequestFactory()
		u = UserView()
		num = random.randint(10, 20)

		for i in range(num):
			user_name = get_random_string(random.randint(10, 20))
			user = {
				"data": {
					"name": user_name,
					"email": get_random_string(random.randint(5, 10)) + email_suffix
				}
			}
			r = user_factory.post('/user/', user, format='json')
			_ = u.post(r)

		users = json.loads(u.get('').content)
		for user in users:
			self.historias.append({
				"data": {
					"name": user['name'],
					"location": get_random_string(random.randint(10, 20)),
					"user_id": user['id']
				}
			})

	def test_get(self):
		factory = APIRequestFactory()
		hv = HistoriaView()
		for historia in self.historias:
			r = factory.post('/historia/', historia, format='json')
			_ = hv.post(r)
		historias = json.loads(hv.get('').content)
		for hist_from_get, hist_inserted in zip(historias, self.historias):
			hist_inserted = hist_inserted['data']
			self.assertEqual(hist_from_get['name'], hist_inserted['name'])
			self.assertEqual(hist_from_get['location'], hist_inserted['location'])
			self.assertEqual(hist_from_get['user'], hist_inserted['user_id'])

	def test_post(self):
		factory = APIRequestFactory()
		for historia in self.historias:
			r = factory.post('/historia/', historia, format='json')
			hv = HistoriaView()
			res = hv.post(r)
			self.assertEqual(res.status_code, requests.status_codes.codes.created)
