from app import app
from flask import request, Flask
from flask_restful import Resource, Api

from getPriceFromTicker import *
from bot import * 



@app.route('/toshi/<messageText>')
def unpackMessage(messageText):
    x=main1(messageText)
    return '''

 <html>
            <head>
                <title>Home Page - Microblog</title>
            </head>
            <body>
                <h1> Welcome to Toshi! </h1>
                <h2> ''' + x + '''</h2> 
            </body>
        </html>'''
