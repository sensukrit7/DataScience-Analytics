# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 05:16:50 2017

@author: bus-superbowl
"""

import pymongo

originIP = "155.97.57.79"  
destIP = "155.97.56.203"   
originCol =  pymongo.MongoClient(originIP,27017)["superbowl"]["sb2018"]   
destCol =  pymongo.MongoClient(destIP,27017)["superbowl"]["sb2018"]

#grab each tweet from origin server insert into dest server
for tweet in originCol.find():
    try:
        destCol.insert_one(tweet)
    except pymongo.errors.DuplicateKeyError:
        pass
    
