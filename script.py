from api_key import *
from new_org_names import *
from helper import *

import requests
import time


log_file = open("log.csv", "w")
log_file.write("Get org status, Org ID, Org Name, Org Domain, Change org name status, New org ID, New org name, New org domain, Note \n")

total_count = len(orgs)
print(total_count)
current_count = 0

for org in orgs:
  current_count = current_count + 1
  url = "https://api.affinity.co/organizations/"

  data = [
    ('name', org['new_org_name']),
  ]
  print("Processing " + str(org['org_id']) + " - " + str(current_count) + " / " + str(total_count))
  # Get org info before change
  response = requests.get(url + org['org_id'], data=data, auth=('', api_key))
  log_file.write(str(response.status_code) + ", " + str(response.json()['id']) + ", " + response.json()['name'] + ", " + response.json()['domain'])

  # Update org with new name and log changes
  response = requests.put(url + org['org_id'], data=data, auth=('', api_key))
  if response.status_code == 200:
    log_file.write(", " + "Success" + ", " + str(response.json()['id']) + ", " + response.json()['name'] + ", " + response.json()['domain'] + "\n")
  else:
    log_file.write(", " + "Uncessful" + ", " + " " + ", " + " " + ", " + " " + str(response.json() + "\n"))


log_file.close()
print("Done!")