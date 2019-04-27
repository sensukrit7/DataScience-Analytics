
# -*- coding: utf-8 -*-
"""
Created on 2/6/2019

@author: bus-superbowl

This script count the number of unique tweets for each brand (we bypass the ads).
It does a OR query equivalent to the following SQL query:
    select count(*) from table where text like ('%keyword%' or '%keyword%') group by tweet_id    
You need to insert one or multiple keywords and comment out the unneeded line of code.
You need to do one brand at a time.

"""

import re
import pymongo

#import collection
col =  pymongo.MongoClient("localhost",27017)["SuperBowl2019"]["SB2019"]
col2 = pymongo.MongoClient("localhost",27017)["SuperBowl2019"]["SB"]

            
#show total tweets in collection (comment out if unneeded)
print "total tweets in SB2019: "
print col.find().count()       

#create the case insensitive LIKE query
#INSERT your keywords below


rgx1 = re.compile('.*pepsi.*', re.IGNORECASE)  # compile the regex
rgx2 = re.compile('.*game of throne.*', re.IGNORECASE)
rgx3 = re.compile('.*marvels.*', re.IGNORECASE)
rgx4 = re.compile('.*hyundai.*', re.IGNORECASE)
rgx5 = re.compile('.*bumble.*', re.IGNORECASE)
rgx6 = re.compile('.*hulu.*', re.IGNORECASE)
rgx7 = re.compile('.*olay.*', re.IGNORECASE)
rgx8 = re.compile('.*doritos.*', re.IGNORECASE)
rgx9 = re.compile('.*bud light.*', re.IGNORECASE)
rgx10 = re.compile('.*simplisafe.*', re.IGNORECASE)
rgx11 = re.compile('.*t mobile.*', re.IGNORECASE)
rgx12 = re.compile('.*audi.*', re.IGNORECASE)
rgx13 = re.compile('.*pringles.*', re.IGNORECASE)
rgx14 = re.compile('.*google.*', re.IGNORECASE)
rgx15 = re.compile('.*mercedes benz.*', re.IGNORECASE)
rgx16 = re.compile('.*percil.*', re.IGNORECASE)
rgx17 = re.compile('.*Toyota.*', re.IGNORECASE)
rgx18 = re.compile('.*planters.*', re.IGNORECASE)
rgx19 = re.compile('.*mintmobile.*', re.IGNORECASE)
rgx20 = re.compile('.*norwegian cruise.*', re.IGNORECASE)
rgx21 = re.compile('.*turbotax.*', re.IGNORECASE)
rgx22 = re.compile('.*Stella Artois.*', re.IGNORECASE)
rgx23 = re.compile('.*Sprint.*', re.IGNORECASE)
rgx24 = re.compile('.*NFL.*', re.IGNORECASE)
rgx25 = re.compile('.*ADT.*', re.IGNORECASE)
rgx26 = re.compile('.*USAA.*', re.IGNORECASE)
rgx27 = re.compile('.*wix.*', re.IGNORECASE)
rgx28 = re.compile('.*Amazon.*', re.IGNORECASE)
rgx29 = re.compile('.*Colgate.*', re.IGNORECASE)
rgx30 = re.compile('.*Skechers.*', re.IGNORECASE)
rgx31 = re.compile('.*devoure.*', re.IGNORECASE)
rgx32 = re.compile('.*Kia.*', re.IGNORECASE)
rgx33 = re.compile('.*Bubly.*', re.IGNORECASE)
rgx34 = re.compile('.*Netflix.*', re.IGNORECASE)
rgx35 = re.compile('.*Ultra.*', re.IGNORECASE)
rgx36 = re.compile('.*Verizon.*', re.IGNORECASE)
rgx37 = re.compile('.*Xfinity.*', re.IGNORECASE)
rgx38 = re.compile('.*minky conture.*', re.IGNORECASE)
rgx39 = re.compile('.*microsoft.*', re.IGNORECASE)
rgx40 = re.compile('.*Ultra.*', re.IGNORECASE)
rgx41 = re.compile('.*Weathertech.*', re.IGNORECASE)
rgx42 = re.compile('.*Burger King.*', re.IGNORECASE)
rgx43 = re.compile('.*Budweisere.*', re.IGNORECASE)
rgx44 = re.compile('.*Alexa.*', re.IGNORECASE)
rgx45 = re.compile('.*Washington Post.*', re.IGNORECASE)
rgx46 = re.compile('.*Avengers.*', re.IGNORECASE)
rgx47 = re.compile('.*gameofthrones.*', re.IGNORECASE)
rgx48 = re.compile('.*mercedesbenz.*', re.IGNORECASE)
rgx49 = re.compile('.*budlight.*', re.IGNORECASE)
rgx50 = re.compile('.*tmobile.*', re.IGNORECASE)
                
				  
result = col.aggregate([
		{ '$match': { '$or': [
                            {'text': {"$regex": rgx1}}
							] }},               
		{ '$group': { '_id': '$id' }}             
      ])
	  
#col2.insert(result)
print "pepsi has ", len(list(result))	  
            
result = col.aggregate([
		{ '$match': { '$or': [
							{'text': {"$regex": rgx2}}
							] }},               
		{ '$group': { '_id': '$id' }}             
      ])
print "game of thrones has" , len(list(result))	  

result = col.aggregate([
		{ '$match': { '$or': [
							{'text': {"$regex": rgx3}}
							] }},               
		{ '$group': { '_id': '$id' }}             
      ])
print "marvels has" , len(list(result))


result = col.aggregate([
		{ '$match': { '$or': [
							{'text': {"$regex": rgx4}}
							] }},               
		{ '$group': { '_id': '$id' }}             
      ])
print "hyundai" , len(list(result))


result = col.aggregate([
		{ '$match': { '$or': [
							{'text': {"$regex": rgx5}}
							] }},               
		{ '$group': { '_id': '$id' }}             
      ])
print "bumble has" , len(list(result))



result = col.aggregate([
		{ '$match': { '$or': [
							{'text': {"$regex": rgx6}}
							] }},               
		{ '$group': { '_id': '$id' }}             
      ])
print "hulu" , len(list(result))


result = col.aggregate([
		{ '$match': { '$or': [
							{'text': {"$regex": rgx7}}
							] }},               
		{ '$group': { '_id': '$id' }}             
      ])
print "olay has" , len(list(result))


result = col.aggregate([
		{ '$match': { '$or': [
							{'text': {"$regex": rgx8}}
							] }},               
		{ '$group': { '_id': '$id' }}             
      ])
print "doritos has" , len(list(result))


result = col.aggregate([
		{ '$match': { '$or': [
							{'text': {"$regex": rgx9}}
							] }},               
		{ '$group': { '_id': '$id' }}             
      ])
print "bud light has" , len(list(result))



result = col.aggregate([
		{ '$match': { '$or': [
							{'text': {"$regex": rgx10}}
							] }},               
		{ '$group': { '_id': '$id' }}             
      ])
print "simplisafe" , len(list(result))


result = col.aggregate([
		{ '$match': { '$or': [
							{'text': {"$regex": rgx11}}
							] }},               
		{ '$group': { '_id': '$id' }}             
      ])
print "tmobile has" , len(list(result))


result = col.aggregate([
		{ '$match': { '$or': [
							{'text': {"$regex": rgx12}}
							] }},               
		{ '$group': { '_id': '$id' }}             
      ])
print "audi has" , len(list(result))


result = col.aggregate([
		{ '$match': { '$or': [
							{'text': {"$regex": rgx13}}
							] }},               
		{ '$group': { '_id': '$id' }}             
      ])
print "pringles has" , len(list(result))


result = col.aggregate([
		{ '$match': { '$or': [
							{'text': {"$regex": rgx14}}
							] }},               
		{ '$group': { '_id': '$id' }}             
      ])
print "google has" , len(list(result))


result = col.aggregate([
		{ '$match': { '$or': [
							{'text': {"$regex": rgx15}}
							] }},               
		{ '$group': { '_id': '$id' }}             
      ])
print "mercedes has" , len(list(result))


result = col.aggregate([
		{ '$match': { '$or': [
							{'text': {"$regex": rgx16}}
							] }},               
		{ '$group': { '_id': '$id' }}             
      ])
print "percil has" , len(list(result))


result = col.aggregate([
		{ '$match': { '$or': [
							{'text': {"$regex": rgx17}}
							] }},               
		{ '$group': { '_id': '$id' }}             
      ])
print "toyota has" , len(list(result))


result = col.aggregate([
		{ '$match': { '$or': [
							{'text': {"$regex": rgx18}}
							] }},               
		{ '$group': { '_id': '$id' }}             
      ])
print "planters has" , len(list(result))


result = col.aggregate([
		{ '$match': { '$or': [
							{'text': {"$regex": rgx19}}
							] }},               
		{ '$group': { '_id': '$id' }}             
      ])
print "mintmob has" , len(list(result))


result = col.aggregate([
		{ '$match': { '$or': [
							{'text': {"$regex": rgx20}}
							] }},               
		{ '$group': { '_id': '$id' }}             
      ])
print "norwegia has" , len(list(result))


result = col.aggregate([
		{ '$match': { '$or': [
							{'text': {"$regex": rgx21}}
							] }},               
		{ '$group': { '_id': '$id' }}             
      ])
print "turbotax has" , len(list(result))



result = col.aggregate([
		{ '$match': { '$or': [
							{'text': {"$regex": rgx22}}
							] }},               
		{ '$group': { '_id': '$id' }}             
      ])
print "stella has" , len(list(result))


result = col.aggregate([
		{ '$match': { '$or': [
							{'text': {"$regex": rgx23}}
							] }},               
		{ '$group': { '_id': '$id' }}             
      ])
print "Spirnt has" , len(list(result))


result = col.aggregate([
		{ '$match': { '$or': [
							{'text': {"$regex": rgx24}}
							] }},               
		{ '$group': { '_id': '$id' }}             
      ])
print "NFL has" , len(list(result))


result = col.aggregate([
		{ '$match': { '$or': [
							{'text': {"$regex": rgx25}}
							] }},               
		{ '$group': { '_id': '$id' }}             
      ])
print "ADT has" , len(list(result))


result = col.aggregate([
		{ '$match': { '$or': [
							{'text': {"$regex": rgx26}}
							] }},               
		{ '$group': { '_id': '$id' }}             
      ])
print "USAA has" , len(list(result))


result = col.aggregate([
		{ '$match': { '$or': [
							{'text': {"$regex": rgx27}}
							] }},               
		{ '$group': { '_id': '$id' }}             
      ])
print "wix has" , len(list(result))


result = col.aggregate([
		{ '$match': { '$or': [
							{'text': {"$regex": rgx28}}
							] }},               
		{ '$group': { '_id': '$id' }}             
      ])
print "Amazon has" , len(list(result))


result = col.aggregate([
		{ '$match': { '$or': [
							{'text': {"$regex": rgx29}}
							] }},               
		{ '$group': { '_id': '$id' }}             
      ])
print "Colgate has" , len(list(result))


result = col.aggregate([
		{ '$match': { '$or': [
							{'text': {"$regex": rgx30}}
							] }},               
		{ '$group': { '_id': '$id' }}             
      ])
print "skechers has" , len(list(result))


result = col.aggregate([
		{ '$match': { '$or': [
							{'text': {"$regex": rgx31}}
							] }},               
		{ '$group': { '_id': '$id' }}             
      ])
print "Devoure has" , len(list(result))

result = col.aggregate([
		{ '$match': { '$or': [
							{'text': {"$regex": rgx32}}
							] }},               
		{ '$group': { '_id': '$id' }}             
      ])
print "KIA has" , len(list(result))


result = col.aggregate([
		{ '$match': { '$or': [
							{'text': {"$regex": rgx33}}
							] }},               
		{ '$group': { '_id': '$id' }}             
      ])
print "Bubly has" , len(list(result))


result = col.aggregate([
		{ '$match': { '$or': [
							{'text': {"$regex": rgx34}}
							] }},               
		{ '$group': { '_id': '$id' }}             
      ])
print "NFlix has" , len(list(result))



result = col.aggregate([
		{ '$match': { '$or': [
							{'text': {"$regex": rgx35}}
							] }},               
		{ '$group': { '_id': '$id' }}             
      ])
print "Ultra has" , len(list(result))


result = col.aggregate([
		{ '$match': { '$or': [
							{'text': {"$regex": rgx36}}
							] }},               
		{ '$group': { '_id': '$id' }}             
      ])
print "Verizon has" , len(list(result))


result = col.aggregate([
		{ '$match': { '$or': [
							{'text': {"$regex": rgx37}}
							] }},               
		{ '$group': { '_id': '$id' }}             
      ])
print "XFi has" , len(list(result))


result = col.aggregate([
		{ '$match': { '$or': [
							{'text': {"$regex": rgx38}}
							] }},               
		{ '$group': { '_id': '$id' }}             
      ])
print "Minky has" , len(list(result))


result = col.aggregate([
		{ '$match': { '$or': [
							{'text': {"$regex": rgx39}}
							] }},               
		{ '$group': { '_id': '$id' }}             
      ])
print "Microsoft has" , len(list(result))


result = col.aggregate([
		{ '$match': { '$or': [
							{'text': {"$regex": rgx40}}
							] }},               
		{ '$group': { '_id': '$id' }}             
      ])
print "Ultra has" , len(list(result))


result = col.aggregate([
		{ '$match': { '$or': [
							{'text': {"$regex": rgx41}}
							] }},               
		{ '$group': { '_id': '$id' }}             
      ])
print "weathertech has" , len(list(result))


result = col.aggregate([
		{ '$match': { '$or': [
							{'text': {"$regex": rgx42}}
							] }},               
		{ '$group': { '_id': '$id' }}             
      ])
print "burger king has" , len(list(result))


result = col.aggregate([
		{ '$match': { '$or': [
							{'text': {"$regex": rgx43}}
							] }},               
		{ '$group': { '_id': '$id' }}             
      ])
print "Bud has" , len(list(result))


result = col.aggregate([
		{ '$match': { '$or': [
							{'text': {"$regex": rgx44}}
							] }},               
		{ '$group': { '_id': '$id' }}             
      ])
print "Alexa has" , len(list(result))


result = col.aggregate([
		{ '$match': { '$or': [
							{'text': {"$regex": rgx45}}
							] }},               
		{ '$group': { '_id': '$id' }}             
      ])
print "WP has" , len(list(result))


result = col.aggregate([
		{ '$match': { '$or': [
							{'text': {"$regex": rgx46}}
							] }},               
		{ '$group': { '_id': '$id' }}             
      ])
print "Avengers has" , len(list(result))




result = col.aggregate([
		{ '$match': { '$or': [
							{'text': {"$regex": rgx47}}
							] }},               
		{ '$group': { '_id': '$id' }}             
      ])
print "GOT has" , len(list(result))


result = col.aggregate([
		{ '$match': { '$or': [
							{'text': {"$regex": rgx48}}
							] }},               
		{ '$group': { '_id': '$id' }}             
      ])
print "MB has" , len(list(result))



result = col.aggregate([
		{ '$match': { '$or': [
							{'text': {"$regex": rgx49}}
							] }},               
		{ '$group': { '_id': '$id' }}             
      ])
print "BL has" , len(list(result))


result = col.aggregate([
		{ '$match': { '$or': [
							{'text': {"$regex": rgx50}}
							] }},               
		{ '$group': { '_id': '$id' }}             
      ])
print "TMO has" , len(list(result))


