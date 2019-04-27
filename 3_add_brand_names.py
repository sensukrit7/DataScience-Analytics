# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 12:44:44 2017

@author: Shambhavi
"""


import pymongo
col =  pymongo.MongoClient("localhost",27017)["superbowl"]["sb2018"]
col.find_one()

#set empty array for all tweets

for tweet in col.find():
    tweetId = tweet["id"]
    emptySet = []
    col.update_one(      {'id': tweetId},                         
                         {'$set': {'brand': emptySet}}, 
                         upsert=False
                         )


# ---------------for budweiser for ad stand_by_you
ct1=0
for tweet in col.find({
                       '$or' : [
                                {'AdTitle': { '$regex' : 'stand_by_you', '$options' : 'i'}}                                
                                ]}):
    ct1 += 1
    
    tweetId = tweet["id"]
    col.update_one(      {'id': tweetId},
                         #addToSet - add item to the existing set, if not exist, will create a new field
                         {'$addToSet': {'brand': "budweiser"}}, 
                         upsert=False
                         )
	
#------#amazonecho
						 
# ---------------for snickers
ct2=0
for tweet in col.find({
                       '$or' : [
                                {'AdTitle': { '$regex' : 'pringles', '$options' : 'i'}}                                
                                ]}):
    ct2 += 1
    
    tweetId = tweet["id"]
    col.update_one(      {'id': tweetId},
                         #addToSet - add item to the existing set, if not exist, will create a new field
                         {'$addToSet': {'brand': "pringles"}}, 
                         upsert=False
                         )
    
    
#print how many has brand field    
print "Number of tweets with brand"
print col.find({'brand': { '$exists': True }}).count()  
print ct1
print ct2    
print col.find({'AdTitle':'stand_by_you'}).count() 
print col.find({'AdTitle':'pringles'}).count()
print col.find({'brand':'budweiser'}).count()
print col.find({'brand':'pringles'}).count()