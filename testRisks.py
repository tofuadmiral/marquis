import requests
import json
from secret import clientId, clientSecret # we import client id and client secret 

auth_data = {
    'grant_type'    : 'client_credentials',
    'client_id'     : 'clientId',
    'client_secret' : 'clientSecret'
}

# create session instance
session = requests.Session()

auth_request = session.post("https://idfs.gs.com/as/token.oauth2", data = auth_data)
access_token_dict = json.loads(auth_request.text)
access_token = access_token_dict["access_token"]

# update session headers with access token
session.headers.update({"Authorization":"Bearer "+ access_token})

id='10516'

request_url = "https://api.marquee.gs.com/v1/assets/{id}/models"

request = session.get(url=request_url)
results = json.loads(request.text)
print(results)