#!/usr/bin/python3

import requests
import json

url_historia = 'http://127.0.0.1:8000/historia/'

headers = {'content-type': 'application/json'}


historia = {
	'name': 'Historia teste 20',
	'location': 'coloqueumcaminhonovoaqui',
	'user_id': '1'
}

dict_historia = {"data": json.dumps(historia)}
requests.post(url_historia, data=dict_historia)
