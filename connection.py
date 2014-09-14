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

# facebookuserid="fantastic" #!!!! to be populated

# post= {"_id": facebookuserid,#facebook userid
# "pts": 0, #sum of your completed challenges
# "completed":[],
# "incomplete":[{"description": "Raise Awareness by Facebook post!", "pval": 10, "name":"challenge1", "status":"incomplete","imgname":"cat2.png"},
# {"description": "Read two articles; educate yourself!", "pval": 5, "name":"challenge2","status":"incomplete","imgname":"cat3.png"},
# {"description": "Raise Awareness", "pval": 10, "name":"challenge3", "status":"incomplete","imgname":"cat2.png"},
# {"description": "Tweet Out", "pval": 10, "name":"challenge4", "status":"incomplete","imgname":"cat2.png"},
# {"description": "Write to the FCC", "pval": 15, "name":"challenge5", "status":"incomplete","imgname":"cat2.png"},
# {"description": "Change Profile Photo", "pval": 5, "name":"challenge6", "status":"incomplete","imgname":"cat2.png"},
# {"description": "Change Cover Photo", "pval": 5, "name":"challenge7", "status":"incomplete","imgname":"cat2.png"}],
# "passed":[]}
# try:
#   posts=db.posts #what is this??
#   post_id=posts.save(post)
#   print post_id
# #  numdocs += 1
# except pymongo.errors.ConnectionFailure, e:
#   print "Could not connect to MongoDB: %s" % e


urls=(
  '/', 'index',
  '/u/(.+)', 'profile', #specifies that stuff comes after the u (user_id)
  '/bye','logout'
)


render = web.template.render('templates')
def RepresentsInt(s):
   try:
       int(s)
       return True
   except ValueError:
       return False


class profile:
  def GET(self, user_id=None):
    try:
      post = client['savethedata']['xxx'].find_one({"_id": user_id})
      if not post and (RepresentsInt(user_id)): #if the user id is not a number, don't do the thing
        post= {"_id": user_id,#facebook userid
        "pts": 0, #sum of your completed challenges
        "all_challenges":[{"description": "Raise Awareness by Facebook post!", "pval": 10, "name":"challenge1", "status":"incomplete","imgname":"cat2.png"},
        {"description": "Read two articles; educate yourself!", "pval": 5, "name":"challenge2","status":"incomplete","imgname":"cat3.png"},
        {"description": "Raise Awareness", "pval": 10, "name":"challenge3", "status":"incomplete","imgname":"cat2.png"},
        {"description": "Tweet Out", "pval": 10, "name":"challenge4", "status":"incomplete","imgname":"cat2.png"},
        {"description": "Write to the FCC", "pval": 15, "name":"challenge5", "status":"incomplete","imgname":"cat2.png"},
        {"description": "Change Profile Photo", "pval": 5, "name":"challenge6", "status":"incomplete","imgname":"cat2.png"},
        {"description": "Change Cover Photo", "pval": 5, "name":"challenge7", "status":"incomplete","imgname":"cat2.png"}]}
        client['savethedata']['xxx'].insert(post)
        #client['savethedata']['xxx'].insert({"user_id": user_id}) //when you go to the profile
    except pymongo.errors.DuplicateKeyError, e:
      print("hello nope")
    print("profile self")
    print(os.getcwd())
    return web.template.render('templates', globals={"post": post}).profile("YOU! (from the web.py)")
    #return render.profile("YOU! (from the web.py)", globals={'posts':[1]})
  def POST(self, user_id=None):
    """update user"""
    challengeid = web.input(name)
    #syntax for updating posts via pymongo
    try:
      post = client['savethedata']['xxx'].update({'_id':user_id}, {"all_challenges": {name:challengeid, "status":"complete"}}},{upsert:true})
      print "update worked!"
    except pymongo.errors.DuplicateKeyError, e:
      print("hello nope")
    return web.template.render('templates', globals={"post":post}).profile("You! (from web.py)")

class logout:
    def GET(self):
 #update in this method (limited in time...)

      print ("logout self")
      print os.getcwd()
      return render.logout("Claire")
class index:
    def GET(self):

      print ("index self")
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
