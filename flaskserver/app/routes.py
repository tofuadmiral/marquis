from app import app
from flask import request, Flask
from flask_restful import Resource, Api

from getPriceFromTicker import *
from bot import * 


@app.route('/toshi/<messageText>')
def unpackMessage(messageText):
    print(messageText)
    x=main1(messageText)
    return x