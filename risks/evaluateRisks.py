from iexfinance import get_historical_data
from datetime import datetime 
from getTickerFromGsid import * 
import pandas as pd 
import csv
import numpy as np
import pickle
import requests
import json

filename='risks'
infile=open(filename, 'rb')
risks=pickle.load(infile)
infile.close()

# now we need to find average risk, 
sum=0
for i in risks:
    sum+=i
avgrisk=sum/(len(risks))

print(avgrisk)

# now classify the risks 
classifiedRisks=[]
onebound=39.22
twobound=78.44
for i in risks:
    if i<onebound:
        classifiedRisks.append(1)
    elif i<twobound and i>onebound:
        classifiedRisks.append(2)
    elif i>twobound:
        classifiedRisks.append(3)

outfile=open('classifiedRisks', 'wb')
pickle.dump(classifiedRisks, outfile)
outfile.close()

