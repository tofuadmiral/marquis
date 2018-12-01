
def getPriceFromName(name):
    import requests
    import json
    from getPrice import getPriceFromTicker
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


    # create a function to get the ticker value of a specific stock from a NAME 

    name_req_url = "https://api.marquee.gs.com/v1/assets/data/query"

    # convert the name to string in case it isn't already a string
    name=str(name)

    name_req_query = {
                    "where": {
                        "name": name
                    },
                    "fields": ["ticker"]
               }
    name_req = session.post(url=name_req_url, json=name_req_query)
    name_results= json.loads(name_req.text)
    tickerresult=name_results["results"][0]["ticker"]
    
    tickerresult=str(tickerresult)

    # now we have the ticker name stored in re sults, so get the price via the name
    return(getPriceFromTicker(tickerresult))

