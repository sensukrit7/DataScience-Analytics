#db.SuperBowl2019.update({"op_stock":{$gte:100}}, { $unset: {"": ""}},{ multi: true });

import re
import pymongo

#import collection
col =  pymongo.MongoClient("localhost",27017)["SuperBowl2019"]["SBreal2"]
col2 = pymongo.MongoClient("localhost",27017)["SuperBowl2019"]["SBreal3"]

count = 1
for tweet in col.find():
	#tweetId = tweet["id"]
	created_at = tweet["created_at"]
	text = tweet["text"]
	#user = tweet["user"]
	#retweet_count = tweet["retweet_count"]
	col2.insert( {'created_at' : created_at, 'text' : text})
	count+=1
	
print("Added ", count, "to db")