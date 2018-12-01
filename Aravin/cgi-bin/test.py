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


GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey",)
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]

PRICE_INPUTS= ("price","value","amount")
PRICE_RESPONSES=("$35.00","$65.00","$85.00")


RISK_INPUTS=("low","medium","high")
RISK_OUTPUTS=("stock1","stock2","stock3")


BUY_INPUTS=("buy","purchase")












# Checking for greetings
def greeting(sentence):
    """If user's input is a greeting, return a greeting response"""
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)


# Checking for stock price
def price(sentence):
    
    for word in sentence.split():
        if word.lower() in PRICE_INPUTS:
            return random.choice(PRICE_RESPONSES)
        
def risk(sentence):
    
    for word in sentence.split():
        if word.lower() in RISK_INPUTS:
            return random.choice(RISK_OUTPUTS)


def buy(sentence):
    
    for word in sentence.split():
        if word.lower() in  BUY_INPUTS:
            return ("Okay..What level of risk are you willing to take (low, medium or high)?")
            


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

flag=True
print("TOSHI: My name is TOSHI. I am here to be your personal invesment helper. If you want to exit, type Bye!")

while(flag==True):
    user_response = input()
    user_response=user_response.lower()
    if(user_response!='bye'):
        if(user_response=='thanks' or user_response=='thank you' ):
            flag=False
            print("TOSHI: You are welcome..")
        else:
            if(greeting(user_response)!=None):
                print("TOSHI: "+greeting(user_response))

            elif(price(user_response)!=None):
                print("TOSHI: "+price(user_response))

            elif(buy(user_response)!=None):
                print("TOSHI: "+buy(user_response))
                risk_bool=True
                
            elif ((risk(user_response))!=None and risk_bool==True):
                print("TOSHI: "+risk(user_response))
                

                
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
