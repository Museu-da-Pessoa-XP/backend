#!/usr/bin/python3

import requests
import json

url_historia = 'http://127.0.0.1:8000/historia/'

headers = {'content-type': 'application/json'}


historia =  {
	'nome': 'Historia teste 20',
	'localizacao': 'coloqueumcaminhonovoaqui',
    'usuario': 'usuario',
}

historias = []
historias.append(historia)

dict_historias = { "data": json.dumps(historias) }
requests.post(url_historia , data=dict_historias)
