import datetime
import pymongo

def date_to_mil(date):
    if isinstance(date, datetime.datetime):
        epoch = datetime.datetime.utcfromtimestamp(0)
        return int((date - epoch).total_seconds())

starttime = date_to_mil(datetime.datetime(2018, 1, 27, 7, 30))   
#starttime = date_to_mil(datetime.datetime(2018, 2, 4, 23, 30))
print("Start Time %d " % starttime)

col =  pymongo.MongoClient("localhost",27017)["superbowl"]["sb2018"]

total=48  #total periods - each is 5 mins long (i.e. minutes)
period=1  #first period
minutes = 60 * 5 
curtime = starttime

while period<=total:
  start = curtime
  print("Period %s " % period)
  print("start time %d " % start)
  curtime += minutes
  end = curtime
  print("end time %d " % end)
    
  #query db to get the tweets fall between start and end time
  #for loop for each then update period id
  
  for tweet in col.find():
    tweet_time = int(tweet["timestamp_ms"])/1000
    if  int((tweet_time >= start) and (tweet_time < end)):
        #print_readable_date(endtime,"End Time")    
        try:
             tweetId = tweet["id"]
             #to add new field 'valid_time' 
             
             col.update_one(
                         {'id': tweetId},
                         {'$set': {'period': period }}, 
                         )
             
        except pymongo.errors.DuplicateKeyError:
            pass         
   
        
  period += 1
  print("==================================")