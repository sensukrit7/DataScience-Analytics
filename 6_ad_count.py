# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 11:04:17 2017

@author: bus-superbowl
"""


import pymongo
col =  pymongo.MongoClient("localhost",27017)["superbowl"]["sb2018"]

#add ad name as needed
ads = ['stand_by_you','pringles','clydasdale']
             
col.find_one()          

'''        
for brand in brands:
    count = 0
    for tweet in col.find():
        try:
            if brand in tweet['brand']:
                count+=1      
        except:
            continue 
    print(brand)
    print(count)
    print("----------------------------------")
'''

for ad in ads:    
    #SQL = select count(*) from sb2018 where ad='ad' group by id
    result = col.aggregate([
              { '$match': { '$and': [{'AdTitle': ad}] }},
              #{ '$group': { '_id': '$id', 'count': { '$sum': 1} }}              
              { '$group': { '_id': '$id' }}        
              ])
    finalcount = len(list(result))
    print ad," has ",finalcount," tweets" 
                