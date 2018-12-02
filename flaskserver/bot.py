import webbrowser
from iexfinance.stocks import Stock
from getPriceFromTicker import *


new=2


# coding: utf-8

# # Meet Robo: your friend

import nltk

# nltk.download() # for downloading packages

import numpy as np
import random
import string # to process standard python strings


f=open('chatbot.txt','r',errors = 'ignore')
raw=f.read()
raw=raw.lower()# converts to lowercase
#nltk.download('punkt') # first-time use only
#nltk.download('wordnet') # first-time use only
sent_tokens = nltk.sent_tokenize(raw)# converts to list of sentences 
word_tokens = nltk.word_tokenize(raw)# converts to list of words


sent_tokens[:2]


word_tokens[:5]


lemmer = nltk.stem.WordNetLemmatizer()
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey")
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]

PRICE_INPUTS= ("price","value","amount")
STOCK_INPUTS=("tsla","fb","aapl","gs")
PRICE_RESPONSES=("$35.00","$65.00","$85.00")


RISK_INPUTS=("low","medium","high")
RISK_OUTPUTS=("stock1","stock2","stock3")


BUY_INPUTS=("buy","purchase")


LEARN_INPUTS=("learn","hearing","learning","understand","knowledgable")

LINKS_INPUTS=("stocks","stock","bonds","bond","cash equivalent","cash","general")












# Checking for greetings
def greeting(sentence):
    """If user's input is a greeting, return a greeting response"""
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)


# Checking for stock price
def price(sentence):
##    
    for word in sentence.split():
        if word.lower() in PRICE_INPUTS:
            for word2 in sentence.split():
                if word2.lower() in STOCK_INPUTS:
                    return str(getPriceFromTicker(word2.lower()))
                else:
                    return ("Please enter a valid ticker symbol")
        
def risk(sentence):
    
    for word in sentence.split():
        if word.lower() in RISK_INPUTS:
            return random.choice(RISK_OUTPUTS)


def buy(sentence):
    
    for word in sentence.split():
        if word.lower() in  BUY_INPUTS:
            return ("Okay..What level of risk are you willing to take (low, medium or high)?")


def learn(sentence):
    
    for word in sentence.split():
        if word.lower() in  LEARN_INPUTS:
            return ("What would you like to learn about? \n 1) Stocks \n 2) Bonds \n 3)Cash Equivalent \n 4)General Investment")
            


def links(sentence):
    
    for word in sentence.split():
        if word.lower() in  LINKS_INPUTS:
            if (word.lower()=="stocks" or word.lower()=="stock"):
                url="https://www.investopedia.com/university/stocks/"
                webbrowser.open(url,new=new)
    

            elif (word.lower()=="bonds" or word.lower()=="bond"):
                url1="https://www.investopedia.com/articles/bonds/08/bond-market-basics.asp"
                webbrowser.open(url1,new=new)
                

            elif (word.lower()=="cash"):
                url2="https://www.accountingcoach.com/blog/item-in-cash-and-cash-equivalents"
                webbrowser.open(url2,new=new)

            elif (word.lower()=="general"):
                url3="https://www.investopedia.com/slide-show/learn-how-to-invest/"
                webbrowser.open(url3,new=new)

            else:
                return("Invalid input.... Please try again")


           
          
            
    return("Hope this helps")




            



from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity






# Generating response
def response(user_response):
    robo_response=''
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        robo_response=robo_response+"I am sorry! I don't understand you"
        return robo_response
    else:
        robo_response = robo_response+sent_tokens[idx]
        return robo_response

risk_bool=False
learn_bool=False

def main1(user_response):

    global risk_bool
    global learn_bool
    global word_tokens
    

    flag=True
    

    
    ##    user_response = input()
    ##    user_response=user_response.lower()
    if(user_response!='bye'):
        if(user_response=='thanks' or user_response=='thank you' ):
            flag=False
            return("TOSHI: You are welcome..")
        else:
            if(greeting(user_response)!=None):
                return("TOSHI: "+greeting(user_response))

            elif(price(user_response)!=None):
                return("TOSHI: "+price(user_response))

            elif(buy(user_response)!=None):
                risk_bool=True
                return("TOSHI: "+buy(user_response))
                
            elif ((risk(user_response))!=None and risk_bool==True):
                return("TOSHI: I would reccommend:\n "+risk(user_response))

            elif ((learn(user_response))!=None and learn_bool==False):
                learn_bool=True
                return("TOSHI: "+learn(user_response))
                

            elif ((links(user_response))!=None and learn_bool):
                learn_bool=False
                return("TOSHI:"+links(user_response))
                
                

                
            else:
                sent_tokens.append(user_response)
                word_tokens=word_tokens+nltk.word_tokenize(user_response)
                final_words=list(set(word_tokens))
                print("TOSHI: ",end="")
                print(response(user_response))
                sent_tokens.remove(user_response)
    else:
        flag=False
        return("TOSHI: Bye! take care..") 

