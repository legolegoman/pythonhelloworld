import requests
from requests_oauthlib import OAuth1

url = "https://api.ciscospark.com/v1/rooms"
auth_t = "OTBjMDhkNTQtZDhiMy00NjRlLWE5YTctYTFiNDA1YTg2OTMyM2YzZGM2MDItZDVl"
headers = {
        'authorization': "Bearer " + auth_t,
        'content-type': "application/json",
    }
output = requests.get(url, headers=headers).json()

i = 0
roomid = []

for _ in output['items']:
    output2 = output['items'][i]
    #print(output2['title'])
    if ("ccp" in str(output2).lower()):
        print(output2['title'],": ",output2['id'])
        roomid.append(output2['id'])
    i += 1

#print(roomid)

j = 0

for _ in roomid:

    url2 = "https://api.ciscospark.com/v1/memberships?roomId={}".format(str(roomid[j]))

    output_member = requests.get(url2, headers=headers).json()

    i = 0

    for _ in output_member['items']:
        out_member_tmp = output_member['items'][i]
        print(out_member_tmp['personDisplayName'],": ",out_member_tmp['personEmail'])
        i += 1

    j += 1
    #print(output_member)
