#!/usr/bin/env python
import pymongo
import sys, os

sys.path.append(os.getcwd())         # XXX might need to be removed
import web
import datetime
from pymongo import MongoClient


# Connection to Mongo DB


# chal1= {"type": "challenge", "description": "Raise Awareness", "ptvalue": 5, "image": "cat.gif"}
# chal2= {"type": "challenge", "description": "Educate Yourself", "ptvalue": 5, "image": "cat.gif"}
# chal3= {"type": "challenge", "description": "Tweet Out", "ptvalue": 5, "image": "cat.gif"}
# chal4= {"type": "challenge", "description": "Write to the FCC", "ptvalue": 5, "image": "cat.gif"}


# post1 = {"name": "Claire",
#         "ptaccum": 10,
#         "openchallenges": ["thing", "test", "number 2"], #assuming this will be linked to another collection later
#         "date": datetime.datetime.utcnow()}


# post= {"user": "karinachan",#facebook userid
#  "pts": 0, #sum of your completed challenges
#  "completed":[{"description": "change your profile picture", "pval": 1, "name":"challenge 0", "status":"complete", "imgname":"cat.png"}],
#  "incomplete":[{"description": "call five people", "pval": 5, "name":"challenge1", "status":"incomplete","imgname":"cat2.png"},
#  {"description": "call five people", "pval": 5, "name":"challenge2","status":"incomplete","imgname":"cat3.png"}],
#  "passed":[{"description":"pour ice bucket water on head and post vid on facebook","pval":10, "name":"challenge3", "status":"passed"}]}

# post1= {"user": "claire",#facebook userid
#  "pts": 0, #sum of your completed challenges
#  "completed":[{"description": "change your profile picture", "pval": 1, "name":"challenge 0", "status":"complete", "imgname":"cat.png"}],
#  "incomplete":[{"description": "call five people", "pval": 5, "name":"challenge1", "status":"incomplete","imgname":"cat2.png"},
#  {"description": "call five people", "pval": 5, "name":"challenge2","status":"incomplete","imgname":"cat3.png"}],
#  "passed":[{"description":"pour ice bucket water on head and post vid on facebook","pval":10, "name":"challenge3", "status":"passed"}]}
try:
  client = MongoClient('mongodb://admin:catmin@ds035240.mongolab.com:35240/savethedata')
  print "Connected successfully!!!"
  db=client['savethedata']
  collection=db['savethedata1']
  print "collection established"
except pymongo.errors.ConnectionFailure, e:
  print "Could not connect to MongoDB: %s" % e

found= False
facebookuserid="cat3" #to be populated and checked if it exists in mongodb already
for item in db.collection.find({"user":facebookuserid}):
  if facebookuserid in item:
    found= True
    print "it exists"


if (found== False):
  post= {"user": facebookuserid,#facebook userid
  "pts": 0, #sum of your completed challenges
  "completed":[],
  "incomplete":[{"description": "Raise Awareness", "pval": 10, "name":"challenge1", "status":"incomplete","imgname":"cat2.png"},
  {"description": "Educate Yourself", "pval": 5, "name":"challenge2","status":"incomplete","imgname":"cat3.png"},
  {"description": "Raise Awareness", "pval": 10, "name":"challenge3", "status":"incomplete","imgname":"cat2.png"},
  {"description": "Tweet Out", "pval": 10, "name":"challenge4", "status":"incomplete","imgname":"cat2.png"},
  {"description": "Write to the FCC", "pval": 15, "name":"challenge5", "status":"incomplete","imgname":"cat2.png"},
  {"description": "Change Profile Photo", "pval": 5, "name":"challenge6", "status":"incomplete","imgname":"cat2.png"},
  {"description": "Change Cover Photo", "pval": 5, "name":"challenge7", "status":"incomplete","imgname":"cat2.png"}],
  "passed":[]}
  try:
    posts=db.posts #what is this??
    post_id=posts.insert(post)
    print post_id
    numdocs += 1
  except pymongo.errors.ConnectionFailure, e:
    print "Could not connect to MongoDB: %s" % e

#print(numdocs)
#if (numdocs == 0):
  # post= {"user": facebookuserid,#facebook userid
  # "pts": 0, #sum of your completed challenges
  # "completed":[],
  # "incomplete":[{"description": "Raise Awareness", "pval": 10, "name":"challenge1", "status":"incomplete","imgname":"cat2.png"},
  # {"description": "Educate Yourself", "pval": 5, "name":"challenge2","status":"incomplete","imgname":"cat3.png"},
  # {"description": "Raise Awareness", "pval": 10, "name":"challenge3", "status":"incomplete","imgname":"cat2.png"},
  # {"description": "Tweet Out", "pval": 10, "name":"challenge4", "status":"incomplete","imgname":"cat2.png"},
  # {"description": "Write to the FCC", "pval": 15, "name":"challenge5", "status":"incomplete","imgname":"cat2.png"},
  # {"description": "Change Profile Photo", "pval": 5, "name":"challenge6", "status":"incomplete","imgname":"cat2.png"},
  # {"description": "Change Cover Photo", "pval": 5, "name":"challenge7", "status":"incomplete","imgname":"cat2.png"}],
  # "passed":[]}
  # try:
  #   posts=db.posts #what is this??
  #   post_id=posts.insert(post)
  #   print post_id
  #   numdocs += 1
  # except pymongo.errors.ConnectionFailure, e:
  #   print "Could not connect to MongoDB: %s" % e




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
