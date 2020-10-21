import requests
import json


url_user = 'http://127.0.0.1:8000/user/'

headers = {'content-type': 'application/json'}


user = {
    'name': 'João 40',
    'email': 'joao@joao.com',
}

dict_user = {"data": json.dumps(user)}
requests.post(url_user, data=dict_user)
