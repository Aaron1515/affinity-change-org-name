from api_key import *
from new_org_names import *
from helper import *

import requests
import time


log_file = open("log.csv", "w")
log_file.write("Get org status, Org ID, Org Name, Org Domain, Change org name status, New org ID, New org name, New org domain, Note \n")

total_count = len(orgs)
current_count = 0

for org in orgs:
  # Start a count of entries
  current_count = current_count + 1

  # Set API URL
  url = "https://api.affinity.co/organizations/"


  data = [
    ('name', org['new_org_name'])
  ]

  # Console log which entry is being process
  print("Processing " + str(org['org_id']) + " - " + str(current_count) + " / " + str(total_count))

  # Get org info before change
  response = requests.get(url + str(org['org_id']), data=data, auth=('', api_key))
  if response.status_code == 200:
    # If there are no domain
    domain = ""
    if response.json()['domain'] == None:
      domain = "No domain found"
    else:
      domain = response.json()['domain']

    log_file.write(str(response.status_code) + ", " + str(response.json()['id']) + ", " + response.json()['name'] + ", " + domain)

    # Update org with new name and log changes
    response = requests.put(url + str(org['org_id']), data=data, auth=('', api_key))
    # Catch no domain found
    domain = ""
    if response.json()['domain'] == None:
      domain = "No domain found"
    else:
      domain = response.json()['domain']

    if response.status_code == 200:
      log_file.write(", " + "Success" + ", " + str(response.json()['id']) + ", " + response.json()['name'] + ", " + domain + "\n")
    else:
      log_file.write(", " + "Uncessful" + ", " + " " + ", " + " " + ", " + " " + str(response.json() + "\n"))
      
  # If org ID can't be found, most likely someone has already changed it.
  elif response.status_code == 422:
    print(response.json())
    log_file.write(str(response.status_code) + ", " + str(response.json()) + "\n")

  # Catch any issues that comes up
  else:
    print(response.json())
    print(response.status_code)
    log_file.write(str(response.status_code) + ", " + "Something went wrong with this org " + str(response.json()) + "\n")


log_file.close()
print("Done!")