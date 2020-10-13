#!/usr/bin/python3

import requests
import json

url_user = 'http://127.0.0.1:8000/user/'

headers = {'content-type': 'application/json'}


user =  {
	'nome': 'João 40',
    'email': 'joao@joao.com',
}

users = []
users.append(user)

dict_users = { "data": json.dumps(users) }
requests.post(url_user , data=dict_users)
