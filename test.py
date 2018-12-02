# this code passes our identifier to the data service to obtain the data from the Query Data endpoint 

import requests
import json

from secret import clientId, clientSecret # we import client id and client secret 
from tickerVals import *
from getPriceFromTicker import *
from getPriceFromName import * 

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
                        "gsid": ["10516","10696","11308","11896","13901"]
                    },
                    "startDate": "2017-01-15",
                    "endDate":"2017-01-16"
               }

request = session.post(url=request_url, json=request_query)
results = json.loads(request.text)


def getSortedGrowths():

    global results

    
    gsids=["10516","10696","11308","11896","13901"]

    scores=[]
    sortd=[]
    tickers=[]

    for i in gsids:
        tickers.append(getTickerFromGsid(i))
        
    for i in range (5):
        scores.append(float(results['data'][i]['growthScore']))


    sortd=scores

    sortd.sort(reverse=True)

    final=[]

    for i in range (5):
        for j in range(5):
            if (sortd[i]==scores[j]):
                final.append(tickers[j]+'-->'+str(sortd[i]))

    return final



def getPortfolio():

    gsids=["10516","10696","11308","11896","13901"]

    scores=[]
    sortd=[]
    tickers=[]

    for i in gsids:
        tickers.append(getTickerFromGsid(i))
    return tickers
    
    

