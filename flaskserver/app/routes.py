from app import app
from flask import request, Flask
from flask_restful import Resource, Api

from getPriceFromTicker import *

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Fuad'}
    x = 20
    y = 20+x
    #y=str(y)
    return '''
<html>
    <head>
        <title>Home Page - Microblog</title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
        <h2> ''' + str(y+y) + ''' </h2> 
    </body>
</html>'''


@app.route('/chatbot/<messageText>')
def processMessage(messageText):
    price = getPriceFromTicker(messageText)    
    price = str(price)
    return price