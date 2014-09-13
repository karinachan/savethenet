#!/usr/bin/env python
import pymongo
import sys, os

sys.path.append(os.getcwd())
import web
import datetime
from pymongo import MongoClient


# Connection to Mongo DB

post = {"author": "Claire",
         "text": "Pymongo insertion #2!",
         "tags": ["pymongo", "test", "number 2"],
         "date": datetime.datetime.utcnow()}

urls=(
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




if __name__ == "__main__":
  print "reached bottom"
  print urls
  print globals()
  print web.reloader
  web.run(urls, globals(), web.reloader)
    #app = web.application(urls, globals())
  #  wsgi_app = web.application(urls, globals()).wsgifunc()
  #  wsgi_app.run()
    #app.run()
