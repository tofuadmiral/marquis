from iexfinance.stocks import Stock

def getPriceFromTicker(tickerval):
    stck = Stock(tickerval)
    return stck.get_price()
