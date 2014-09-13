import pymongo
import datetime
from pymongo import MongoClient


# Connection to Mongo DB

post = {"author": "Karina",
         "text": "Pymongo insertion #1!",
         "tags": ["pymongo", "test", "number 1"],
         "date": datetime.datetime.utcnow()}


try:
    client = MongoClient('mongodb://admin:catmin@ds035240.mongolab.com:35240/savethedata')
    print "Connected successfully!!!"
    db=client['savethedata']
    collection=db['savethedata1']
    print "collection established"
    posts=db.posts
    post_id=posts.insert(post)
    print post_id

except pymongo.errors.ConnectionFailure, e:
   print "Could not connect to MongoDB: %s" % e
