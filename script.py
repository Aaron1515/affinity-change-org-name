from api_key import *
from file_ids import *
from helper import *

import requests
import time


api_key = 'API KEY'


entries = [
  {"opp_id": "2420457", "opp_name": "new opp name"},
  {"opp_id": "2420468", "opp_name": "new opp name"}
  ]

for x in entries:

  url = "https://api.affinity.co/opportunities/"

  data = [
    ('name', x['opp_name']),
  ]

  response = requests.put(url+x['opp_id'], data=data, auth=('', api_key))

  json = response.json()

  print(response.status_code)
  print(json)
  print(" ")