import pymongo
import web
import datetime
from pymongo import MongoClient


# Connection to Mongo DB

post = {"author": "Claire",
         "text": "Pymongo insertion #2!",
         "tags": ["pymongo", "test", "number 2"],
         "date": datetime.datetime.utcnow()}

urls=(
  '/', 'profile',
  '/logout','logout'
)

class profile:
    def GET(self):
      render = web.template.render('templates/profile.html')
      return render.profile("YOU! (from the web.py)")

class bye:
    def GET(self):
      render = web.template.render('templates/logout.html')
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
    app = web.application(urls, globals())
    app.run()
