# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 00:00:25 2017

@author: bus-superbowl
"""
import pymongo
col =  pymongo.MongoClient("localhost",27017)["superbowl"]["sb2018"]
#col.find_one()

#set empty array for all tweets
for tweet in col.find():
    tweetId = tweet["id"]
    emptySet = []
    col.update_one(      {'id': tweetId},                         
                         {'$set': {'AdTitle': emptySet}}, 
                         upsert=False
                         )

'''
#####################################################################
#for budweiser ad
for tweet in col.find({
          '$or' : [
                   {'text': { '$regex' : '#budweiser', '$options' : 'i'}},
                   {'text': { '$regex' : 'budweiser', '$options' : 'i'}},
                   {'text': { '$regex' : 'standbyyou', '$options' : 'i'}},
                   {'text': { '$regex' : '#standbyyou', '$options' : 'i'}}
                   ]
              }):
    tweetId = tweet["id"]
    col.update_one(      {'id': tweetId},
                         #addToSet - add item to the existing set, if not exist, will create a new field
                         {'$addToSet': {'AdTitle': "stand_by_you"}}, 
                         upsert=False
                         )
#####################################################################
#for pringles ad    
for tweet in col.find({
          '$or' : [
                   {'text': { '$regex' : '#pringles', '$options' : 'i'}},
                   {'text': { '$regex' : 'pringles', '$options' : 'i'}},
                   {'text': { '$regex' : '#wow', '$options' : 'i'}}
                  ]
              }):
    tweetId = tweet["id"]
    col.update_one(      {'id': tweetId},
                         {'$addToSet': {'AdTitle': "pringles"}}, 
                         upsert=False
                         )    

#####################################################################
'''
