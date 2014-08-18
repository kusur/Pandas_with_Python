#!/usr/bin/env python

import pandas as pd
from pandas import DataFrame
import datetime
import pandas.io.data


#start = datetime.datetime(2000,1,1)
#end = datetime.datetime(2014,1,1)

#sp500 = pandas.io.data.get_data_yahoo('^GSPC',start,end)

#sp500.to_csv('google2csv.csv')

share = pd.read_csv('google2csv.csv',index_col='Date')

#print share.head()

info1 = share['Close']

print info1.head()

info2 = share[['Open','Close']]

print info2.head()

#del info2['Open']

#print info2.head()

info2.rename(columns={'Close':'CLOSE','Open':'OPEN'},inplace=True)

print info2.head()

info3 = info2

print info3.head()

info4 = info3[(info3['OPEN']>1400)]

print info4
