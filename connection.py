#!/usr/bin/env python
import pymongo
import sys, os

sys.path.append(os.getcwd())         # XXX might need to be removed
import web
import datetime
from pymongo import MongoClient


# Connection to Mongo DB


post= {"description": "Test challenge", "ptvalue": 5, "image":"cat.gif"}


post1 = {"name": "Claire",
        "ptaccum": 10,
        "openchallenges": ["thing", "test", "number 2"], #assuming this will be linked to another collection later
        "date": datetime.datetime.utcnow()}

urls=(
  '/', 'index',
  '/u', 'profile',
  '/bye','logout'
)


render = web.template.render('templates')

class profile:
    def GET(self):
      print os.getcwd()
      return render.profile("YOU! (from the web.py)")

class logout:
    def GET(self):
      print os.getcwd()
      return render.logout("Claire")
class index:
    def GET(self):
      print os.getcwd()
      return render.index("YAY")
try:
    client = MongoClient('mongodb://admin:catmin@ds035240.mongolab.com:35240/savethedata')
    print "Connected successfully!!!"
    db=client['savethedata']
    collection=db['savethedata1']
    print "collection established"
    posts=db.posts #what is this??
    post_id=posts.insert(post)
    print post_id
    post_id2=posts.insert(post1)
    print post_id2

except pymongo.errors.ConnectionFailure, e:
   print "Could not connect to MongoDB: %s" % e


app = web.application(urls, globals())

if __name__ == "__main__":
  print "reached bottom"
  print urls
  print globals()
  # print web.reloader
  # web.run(urls, globals(), web.reloader)
  app.run()
    #app = web.application(urls, globals())
  #  wsgi_app = web.application(urls, globals()).wsgifunc()
  #  wsgi_app.run()
    #app.run()
