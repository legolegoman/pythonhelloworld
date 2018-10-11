import requests
from requests.auth import HTTPBasicAuth
import json

#url = "https://10.1.5.19/api/system/v1/auth/token"
url = "https://dnac2.cisco.com/api/system/v1/auth/token"

headers = {'content-type': 'application/json'}

#resp = requests.post(url, auth=HTTPBasicAuth(username='admin', password='C1sc0123'), headers=headers,verify=False)
resp = requests.post(url, auth=HTTPBasicAuth(username='cisco', password='CiscoDNA!'), headers=headers,verify=False)

print ("Request Status: ",resp.status_code)


token = resp.json()['Token']

print(token)
