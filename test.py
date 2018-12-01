# this code passes our identifier to the data service to obtain the data from the Query Data endpoint 

import requests
import json

from secret import clientId, clientSecret # we import client id and client secret mostly, those r the ones we want

auth_data = {
    "grant_type"    : "client_credentials",
    "client_id"     : clientId,
    "client_secret" : clientSecret,
    "scope"         : "read_product_data"
}

# create session instance
session = requests.Session()

auth_request = session.post("https://idfs.gs.com/as/token.oauth2", data = auth_data)
access_token_dict = json.loads(auth_request.text)
access_token = access_token_dict["access_token"]

# update session headers with access token
session.headers.update({"Authorization":"Bearer "+ access_token})

request_url = "https://api.marquee.gs.com/v1/data/USCANFPP_MINI/query"

request_query = {
                    "where": {
                        "gsid": ["901237","11308","177256"]
                    },
                    "startDate": "2017-01-15",
                    "endDate":"2018-01-15"
               }

request = session.post(url=request_url, json=request_query)
results = json.loads(request.text)

print(results)

print ('  ________  ')
print ('  ________  ')
print ('  ________  ')
print ('  ________  ')

# can successfully get the data and access certain keys

print(results['data'][0]['date'])

print ('  ________  ')
print ('  ________  ')
print ('  ________  ')
print ('  ________  ')

# now, let's map our gsids to our actual tickers and tosee performances 

gsid_req_url = "https://api.marquee.gs.com/v1/assets/data/query"

gsid_req_query = {
                    "where": {
                        "gsid": ["901237","11308","177256"]
                    },
                    "startDate": "2017-01-15",
                    "endDate":"2018-01-15"
               }
