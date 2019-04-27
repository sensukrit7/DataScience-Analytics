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
rgx2 = re.compile('.*game of thrones.*', re.IGNORECASE)
rgx3 = re.compile('.*gameofthrones.*', re.IGNORECASE)
rgx4 = re.compile('.*game of throne.*', re.IGNORECASE)
rgx5 = re.compile('.*GOT.*', re.IGNORECASE)
rgx6 = re.compile('.*marvels.*', re.IGNORECASE)
rgx7 = re.compile('.*avengers.*', re.IGNORECASE)
rgx8 = re.compile('.*budweiser.*', re.IGNORECASE)
rgx9 = re.compile('.*budlight.*', re.IGNORECASE)
rgx10 = re.compile('.*amazon.*', re.IGNORECASE)
rgx11 = re.compile('.*alexa.*', re.IGNORECASE)
rgx12 = re.compile('.*netflix.*', re.IGNORECASE)
rgx13 = re.compile('.*microsoft.*', re.IGNORECASE)
rgx14 = re.compile('.*verizon.*', re.IGNORECASE)  


result = col.aggregate([
		{ '$match': { '$or': [
                            {'text': {"$regex": rgx1}}
							] }},               
		{ '$group': { '_id': '$id' }}             
      ])
	  
col2.insert(result)
print "pepsi has ", len(list(result))	 
 
            
result = col.aggregate([
		{ '$match': { '$or': [
							{'text': {"$regex": rgx2}}
							] }},               
		{ '$group': { '_id': '$id' }}             
      ])
col2.insert(result)	  
print "GOT-1 has" , len(list(result))	  



result = col.aggregate([
		{ '$match': { '$or': [
							{'text': {"$regex": rgx3}}
							] }},               
		{ '$group': { '_id': '$id' }}             
      ])
col2.insert(result)
print "GOT-2 has" , len(list(result))


result = col.aggregate([
		{ '$match': { '$or': [
							{'text': {"$regex": rgx4}}
							] }},               
		{ '$group': { '_id': '$id' }}             
      ])
col2.insert(result)
print "GOT-3 has" , len(list(result))


result = col.aggregate([
		{ '$match': { '$or': [
							{'text': {"$regex": rgx5}}
							] }},               
		{ '$group': { '_id': '$id' }}             
      ])
col2.insert(result)
print "GOT-4 has" , len(list(result))



result = col.aggregate([
		{ '$match': { '$or': [
							{'text': {"$regex": rgx6}}
							] }},               
		{ '$group': { '_id': '$id' }}             
      ])
col2.insert(result)
print "Marvel-1" , len(list(result))


result = col.aggregate([
		{ '$match': { '$or': [
							{'text': {"$regex": rgx7}}
							] }},               
		{ '$group': { '_id': '$id' }}             
      ])
col2.insert(result)	  
print "Marvel-2 has" , len(list(result))


result = col.aggregate([
		{ '$match': { '$or': [
							{'text': {"$regex": rgx8}}
							] }},               
		{ '$group': { '_id': '$id' }}             
      ])
col2.insert(result)
print "BUD-1 has" , len(list(result))


result = col.aggregate([
		{ '$match': { '$or': [
							{'text': {"$regex": rgx9}}
							] }},               
		{ '$group': { '_id': '$id' }}             
      ])
col2.insert(result)
print "BUD-2 has" , len(list(result))



result = col.aggregate([
		{ '$match': { '$or': [
							{'text': {"$regex": rgx10}}
							] }},               
		{ '$group': { '_id': '$id' }}             
      ])
col2.insert(result)
print "Amazon-1" , len(list(result))


result = col.aggregate([
		{ '$match': { '$or': [
							{'text': {"$regex": rgx11}}
							] }},               
		{ '$group': { '_id': '$id' }}             
      ])
col2.insert(result)
print "Amazon-2" , len(list(result))


result = col.aggregate([
		{ '$match': { '$or': [
							{'text': {"$regex": rgx12}}
							] }},               
		{ '$group': { '_id': '$id' }}             
      ])
col2.insert(result)
print "Netflix" , len(list(result))


result = col.aggregate([
		{ '$match': { '$or': [
							{'text': {"$regex": rgx13}}
							] }},               
		{ '$group': { '_id': '$id' }}             
      ])
col2.insert(result)
print "Microsft has" , len(list(result))


result = col.aggregate([
		{ '$match': { '$or': [
							{'text': {"$regex": rgx14}}
							] }},               
		{ '$group': { '_id': '$id' }}             
      ])
col2.insert(result)
print "Verizon has" , len(list(result))

