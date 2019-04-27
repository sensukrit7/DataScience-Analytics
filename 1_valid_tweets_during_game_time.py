# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 13:50:48 2017

@author: bus-superbowl
"""

import pymongo
import datetime

# this method converts the time stamp into seconds
def date_to_mil(date):
    if isinstance(date, datetime.datetime):
        epoch = datetime.datetime.utcfromtimestamp(0)
        return float((date - epoch).total_seconds())

def print_readable_date(stringdate,caption):
    print caption
    print(
          datetime.datetime.fromtimestamp(int(stringdate)).strftime('%Y-%m-%d %H:%M:%S')
    )
    print('===================================')
               
col =  pymongo.MongoClient("localhost",27017)["superbowl"]["sb2018"]

#year, month, day, hour, min (GMT time)
gamestart = date_to_mil(datetime.datetime(2018, 2, 4, 23, 30)) 
print_readable_date(gamestart,"Game Start Time") 
gameend = date_to_mil(datetime.datetime(2018, 2, 5, 3, 30)) 
print_readable_date(gameend,"Game End Time") 

'''
starttime = date_to_mil(datetime.datetime(2018, 1, 27, 7, 0))  
print_readable_date(starttime,"Start Time") 
endtime = date_to_mil(datetime.datetime(2018, 1, 27, 19, 0))  
print_readable_date(endtime,"End Time") 
'''

#find all tweets of english language only
'''
for tweet in col.find({'lang':'en'}):
    # to replace with gamestart and gameend for the SuperBowl 
    tweet_time = int(tweet["timestamp_ms"])/1000
    if  int((tweet_time >= gamestart) and (tweet_time <= gameend)):
        #print_readable_date(endtime,"End Time")    
        try:
             tweetId = tweet["id"]
             #to add new field 'valid_time' 
             col.update_one(
                         {'id': tweetId},
                         {'$set': {'valid_time': "1"}}, 
                         )
        except pymongo.errors.DuplicateKeyError:
            pass         
        
       
print "total tweets in the dataset "        
print col.find().count()  
print "total valid tweets between gamestart and gameend "        
print col.find({'valid_time' : "1"}).count()  

#remove invalid tweets
print "removing invalid tweets"
print col.find({'valid_time': { '$exists': False }}).count()   
col.delete_many({'valid_time': { '$exists': False }})
print "DONE...."
'''