import requests
from requests_oauthlib import OAuth1


url = "https://api.ciscospark.com/v1/people?email=ivanwwon@cisco.com"
auth_t = "OTBjMDhkNTQtZDhiMy00NjRlLWE5YTctYTFiNDA1YTg2OTMyM2YzZGM2MDItZDVl"
headers = {
        'authorization': "Bearer " + auth_t,
        'content-type': "application/json",
    }
output = requests.get(url, headers=headers).json()

print(output['items'])

output2 = output['items'][0]

print(output2['displayName'])
