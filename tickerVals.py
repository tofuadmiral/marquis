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

############################ ALL THE ABOVE WAS TO GET THE PERMISSIONS FROM THE SERVER ########################################

# now, let's map our gsids to our actual tickers and to see prices 

# create a function to get the ticker value of a specific stock GSID

def getTickerFromGsid(gsid):
    gsid_req_url = "https://api.marquee.gs.com/v1/assets/data/query"

    gsid_req_query = {
                    "where": {
                        "gsid": gsid
                    },
                    "fields": ["ticker"]
               }

    gsid_req = session.post(url=gsid_req_url, json=gsid_req_query)
    gsid_results= json.loads(gsid_req.text)
    return gsid_results