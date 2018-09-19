import http.client

conn = http.client.HTTPConnection("10.1.5.19")

headers = {
    'X-Auth-Token': "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI1YjdhMmY5MTc1ODcwODAwOGNkZjEyZTEiLCJhdXRoU291cmNlIjoiaW50ZXJuYWwiLCJ0ZW5hbnROYW1lIjoiVE5UMCIsInJvbGVzIjpbIjViN2EyZjhmNzU4NzA4MDA4Y2RmMTJlMCJdLCJ0ZW5hbnRJZCI6IjViN2EyZjhlNzU4NzA4MDA4Y2RmMTJkZSIsImV4cCI6MTUzNzM1NzUwNywidXNlcm5hbWUiOiJhZG1pbiJ9.pXBLbE3Ua0_iqmCA50uu4npotNKUJkaeD7D2lb-CD-c",
    'Cache-Control': "no-cache",
    'Postman-Token': "4e6274ef-29b6-4f0c-a6a7-b4a012719675"
    }

conn.request("GET", "api,v1,network-device", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
