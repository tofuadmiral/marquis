from iexfinance import get_historical_data
from datetime import datetime 
from getTickerFromGsid import * 
import pandas as pd 
import csv
import numpy as np
import pickle

######################################################  get goldman info 
import requests
import json

from secret import clientId, clientSecret # we import client id and client secret 

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
                    "startDate": "2015-02-15",
                    "endDate":"2016-03-16"
               }

request = session.post(url=request_url, json=request_query)
results = json.loads(request.text)

## iterate through the results to get unique GSIDs only 
## add to dictionary if not in the dictionary 
gsids=[]
for i in results['data']:
    if i['gsid'] not in gsids:
        gsids.append(i['gsid']) # should be 100 stocks here! :)


############################################################################################################

# write the gsids to a csv and write the ticker values
tickers=[]
for i in gsids:
    tickers.append(getTickerFromGsid(i))


## now we have tickers, so get historical pricing for each of the 100 stocks and store in dataframes

# getting prices for the last year
start=datetime(2017, 12, 1)
end=datetime.today()

prices=[]
for i in tickers:
    df = get_historical_data(i, start=start, end=end, output_format='pandas')
    prices.append(df)

# now we have all prices, so process it to get risk values. let's use std dev as a proxy for the risk
averages=[]
for i in prices:
    sum=0
    for index, row in i.iterrows(): # iterate over the rows
        sum+=row['open']
    averages.append(sum/(len(i.index)))

# with averages, take the std deviations
risks=[]
for i in prices:
    counter=0
    sumdiffs=0
    for index, row in i.iterrows():
        sumdiffs+=(row['open']-averages[counter])
    counter+=1
    risks.append(sumdiffs/(len(i.index)))

print(risks[0])


# store for further usage 
outfile=open('gsids', 'wb')
pickle.dump(gsids, outfile)
outfile.close()

outfile=open('tickers', 'wb')
pickle.dump(tickers, outfile)
outfile.close()

outfile=open('prices', 'wb')
pickle.dump(prices, outfile)
outfile.close()

outfile=open('averages', 'wb')
pickle.dump(averages, outfile)
outfile.close()

outfile=open('risks', 'wb')
pickle.dump(risks, outfile)
outfile.close()

