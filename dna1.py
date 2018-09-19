import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://10.1.5.19/api/system/v1/auth/token"

headers = {'content-type': 'application/json'}

resp = requests.post(url, auth=HTTPBasicAuth(username='admin', password='C1sc0123'), headers=headers,verify=False)

print ("Request Status: ",resp.status_code)


token = resp.json()['Token']

#print(token)

url = "https://10.1.5.19/api/v1/network-device"

headers = {'X-Auth-Token': token}

resp = requests.get(url, headers=headers,verify=False)

print ("Request Status: ",resp.status_code)

networkdevice = resp.json()

i = 0


for _ in networkdevice['response']:
    networkdevice_tmp = networkdevice['response'][i]
    print(networkdevice_tmp['platformId'],": ",networkdevice_tmp['hostname']," ",networkdevice_tmp['id'])
    i += 1
