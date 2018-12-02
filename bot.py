import webbrowser
from iexfinance.stocks import Stock
from getPriceFromTicker import *
from test import *
import pickle 


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

BUY1_INPUTS=("20","30","40","50","60","70")

BUY2_INPUTS=("20000","30000","40000","50000","60000","70000")

BUY3_INPUTS=("short","long")



LEARN_INPUTS=("learn","hearing","learning","understand","knowledgable")
LINKS_INPUTS=("stocks","stock","bonds","bond","cash equivalent","cash","general")


PORTFOLIO_INPUTS=("see")

GROWTH_INPUTS=("growth","grow","expand")










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
            
            filename="./risks/classifiedRisks"
            infile=open(filename, "rb")
            crisks=pickle.load(infile)
            infile.close()

            filename2="./risks/tickers"
            infile1=open(filename2, "rb")
            tick=pickle.load(infile1)
            infile1.close()

            stocks=[]
            x=0

            if (word.lower()=="low"):
                for i in crisks:
                    if (i==1):
                        stocks.append(tick[x])
                    x=x+1

            elif (word.lower()=="medium"):
                for i in crisks:
                    if (i==2):
                        stocks.append(tick[x])
                    x=x+1

            elif (word.lower()=="high"):
                for i in crisks:
                    if (i==3):
                        stocks.append(tick[x])
                    x=x+1
        
                        

    return stocks
                        
                        
                    

    
risk_count=0



def buy(sentence):
    
    for word in sentence.split():
        if word.lower() in  BUY_INPUTS:
            return ("Okay..We will need to run a quick risk tolerence assesment?\n Q1) How old are you?")

def buy1(sentence):

    global risk_count
    
    for word in sentence.split():
        if word.lower() in  BUY1_INPUTS:

            if(int(word.lower())<=30):
                risk_count=risk_count+1
            
            return ("Q2) What is your annual income?")

def buy2(sentence):

    global risk_count
    
    for word in sentence.split():
        if word.lower() in  BUY2_INPUTS:

            if(int(word.lower())<=50000):
                risk_count=risk_count+1
            
            return ("Q3) Are you looking for short term or long term gain?")

def buy3(sentence):

    global risk_count
    
    for word in sentence.split():
        if word.lower() in  BUY3_INPUTS:

            if(word.lower()=="short"):
                risk_count=risk_count+1
            
            return ("Your Risk Assesment Has Beeen Complete!\n following are some reccomended stock quotes for your particular risk tolerence")

def learn(sentence):
    
    for word in sentence.split():
        if word.lower() in  LEARN_INPUTS:
            return ("What would you like to learn about? \n 1) Stocks \n 2) Bonds \n 3)Cash Equivalent \n 4)General Investment")

def portfolio(sentence):
    
    for word in sentence.split():
        if word.lower() in  PORTFOLIO_INPUTS:
            return (getPortfolio())

def growthRank(sentence):

     for word in sentence.split():
        if word.lower() in  GROWTH_INPUTS:
            return (getSortedGrowths())


            


            


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



   
flag=True

print("********************************************************************************\n                         WELCOME TO MARQUIS                     \n********************************************************************************\n\n" ) 


print("CHAT HERE\n-------------\n\n")

print("Hello.. My Name is Toshi, welcome to your personalized investment experience")



while(flag==True):
    print("Your Message:")
    user_response = input()
    user_response=user_response.lower()
    if(user_response!='bye'):
        if(user_response=='thanks' or user_response=='thank you' ):
            flag=False
            print("TOSHI: You are welcome..")
        else:
            if(greeting(user_response)!=None):
                print("TOSHI: "+greeting(user_response))
                print("\n")
    
            elif(price(user_response)!=None):
                print("TOSHI: "+price(user_response))
                print("\n")

            elif(buy(user_response)!=None):
                print("TOSHI: "+  str(buy(user_response)))
                print("\n")

            elif(buy1(user_response)!=None):
                print("TOSHI: "+  buy1(user_response))
                print("\n")

            elif(buy2(user_response)!=None):
                print("TOSHI: "+  buy2(user_response))
                print("\n")

            elif(buy3(user_response)!=None):
                print("TOSHI: "+  buy3(user_response))


                if (risk_count==1):
                    l=risk("low")
                    
                elif(risk_count==2):
                    l=risk("medium")
                    
                else:
                    l=risk("high")

                for i in l:
                    print(i)

                
                risk_bool=True
                print("\n")
                
##            elif ((risk(user_response))!=None):
##                print("TOSHI: I would reccommend the following stocks:\n ") 
##                s=risk(user_response)
##
##                for i in s:
##                    print(i)
##                
##                
##                print("\n")

            elif ((learn(user_response))!=None and learn_bool==False):
                print("TOSHI: "+learn(user_response))
                learn_bool=True
                print("\n")

            elif ((links(user_response))!=None and learn_bool):
                print("TOSHI:"+links(user_response))
                learn_bool=False
                print("\n")
    
            elif ((portfolio(user_response))!=None):
                print("TOSHI:")
                x=portfolio(user_response)
                for i in x:
                    print(i)
                print("\n")
                

            elif (growthRank(user_response)):
                print("TOSHI: Here is the rank of all of your investments growth: \n")
                x=growthRank(user_response)
                for i in x:
                    print(i)
                print("\n")
        

                

                
            else:
                sent_tokens.append(user_response)
                word_tokens=word_tokens+nltk.word_tokenize(user_response)
                final_words=list(set(word_tokens))
                print("TOSHI: ",end="")
                print(response(user_response))
                sent_tokens.remove(user_response)
    else:
        flag=False
        print("TOSHI: Bye! take care..") 


