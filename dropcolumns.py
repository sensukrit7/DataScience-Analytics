import re
import pymongo

#import collection
col =  pymongo.MongoClient("localhost",27017)["SuperBowl2019"]["SB2019"]
col2 = pymongo.MongoClient("localhost",27017)["SuperBowl2019"]["SB2"]


result = col2.aggregate(
		{"$or" : [ 
							{'text': {"$regex":rgx1}},
                            {'text': {"$regex": rgx1}},
							{'text': {"$regex": rgx2}},
							{'text': {"$regex": rgx3}},
							{'text': {"$regex": rgx4}},
							{'text': {"$regex": rgx5}},
							{'text': {"$regex": rgx6}},
							{'text': {"$regex": rgx7}},
							{'text': {"$regex": rgx8}},
							{'text': {"$regex": rgx9}},
							{'text': {"$regex": rgx10}},
							{'text': {"$regex": rgx11}},
							{'text': {"$regex": rgx12}},
							{'text': {"$regex": rgx13}},
							{'text': {"$regex": rgx14}}
							]}  
		{'$group' : { '_id' : $id}}
      )
	  
col2.insert(result)
print len(list(result))	