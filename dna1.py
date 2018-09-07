import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://198.18.129.100/api/system/v1/auth/token"

headers = {'content-type': 'application/json'}

resp = requests.post(url, auth=HTTPBasicAuth(username='admin', password='C1sco12345'), headers=headers,verify=False)

print ("Request Status: ",resp.status_code)


#token = resp.json()['Token']


#print(token)
