# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 18:27:11 2017

@author: bus-superbowl
"""

import re
import HTMLParser
from textblob import TextBlob
import pymongo


col =  pymongo.MongoClient("localhost",27017)["superbowl"]["sb2018"]
col.count()

def linkify_tweet(tweet):
    print re.search(r'#([^\s]+)',tweet)
    tweet = re.sub(r'(\A|\s)@(\w+)', r'\1@<a href="http://www.twitter.com/\2">\2</a>', tweet)
    return re.sub(r'(\A|\s)#(\w+)', r'\1#<a href="http://search.twitter.com/search?q=%23\2">\2</a>', tweet)
  
#print linkify_tweet("best day ever #coke #pepsi")
    
# sentiment script
def processTweet(tweet):    
    tweet = re.sub('@[^\s]+','',tweet)#remove @ 
    parser = HTMLParser.HTMLParser()
    tweet= parser.unescape(tweet) # process the tweets
    tweet = tweet.lower()#Convert to lower case
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+)|(http[^\s]+))','',tweet)#remove www.* or https?://* 
    tweet = re.sub('[^a-zA-Z0-9 \n\.]', '', tweet)#consider only aplhabets
    tweet = re.sub('b4','before',tweet) #replace b4
    tweet = re.sub('[\s]+', ' ', tweet) #Remove additional white spaces
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet) #remove hashtags
    tweet = tweet.strip('\'"')#trim
    return tweet


#for test, uncomment all the lines below
#you should see sentiment processing for 100 tweets    
#ct=0
for tweet in col.find():
    tweetId = tweet["id"]
    
    tweetText = tweet["text"]
    #print tweetText

    processedTestTweet = processTweet(tweetText)
    #print processedTestTweet
    
    testimonial = TextBlob(processedTestTweet)
    pol = testimonial.sentiment.polarity
    if (pol>0):
        outcome =1
    elif(pol<0):
        outcome =- 1
    elif(pol==0):
        outcome = 0
    
    #print outcome    
    #print '==================================================================='
    
    
    #ct += 1
    #if ct==100:
    #    break    
        
    col.update_one(
                         {'id': tweetId},
                         {'$set': {'sentiment': outcome,  'polarity': pol}}, 
                         upsert=False
                         )

'''
print "=== Sentiment Report ==="
print "Total tweets for budweiser: %d" % col.find({'brand':'budweiser'}).count()

print "Budweiser positive: %d" % col.find({ '$and': [{'brand':'budweiser'},{'sentiment': 1}] }).count() 
print "Budweiser neutral: %d" % col.find({ '$and': [{'brand':'budweiser'},{'sentiment': 0}] }).count() 
print "Budweiser negative: %d" % col.find({ '$and': [{'brand':'budweiser'},{'sentiment': -1}] }).count() 
print "============================================================="
print "Total tweets for pringles: %d" % col.find({'brand':'pringles'}).count()
print "Pringles positive: %d" % col.find({ '$and': [{'brand':'pringles'},{'sentiment': 1}] }).count() 
print "Pringles neutral: %d" % col.find({ '$and': [{'brand':'pringles'},{'sentiment': 0}] }).count() 
print "Pringles negative: %d" % col.find({ '$and': [{'brand':'pringles'},{'sentiment': -1}] }).count() 


result = col.aggregate([
              { '$match': { '$and': [{'brand':'pringles'},{'sentiment': -1}] }},
              #{ '$group': { '_id': '$id', 'count': { '$sum': 1} }}              
              { '$group': { '_id': '$id' }}        
              ])

print len(list(result))
'''