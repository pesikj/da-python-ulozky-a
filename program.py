import requests
import json
import sys
from datetime import date
response = requests.get('http://svatky.adresa.info/json')
svatek_dnes = json.loads(response.text)
print(svatek_dnes[0]['name'])

DDMM = sys.argv[1]
response = requests.get('https://svatky.adresa.info/json?date=' + DDMM)
svatek = json.loads(response.text)
print(svatek[0]['name'])
