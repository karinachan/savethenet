from flask import Flask, render_template, request, url_for
import pymongo
import sys, os
import datetime
from pymongo import MongoClient
app = Flask(__name__)

application = app # For AWS EBS

try:
  client = MongoClient('mongodb://admin:catmin@ds035240.mongolab.com:35240/savethedata')
  print "Connected successfully!!!"
  db=client['savethedata']
  collection=db['xxx']
  print "collection established"
except pymongo.errors.ConnectionFailure, e:
  print "Could not connect to MongoDB: %s" % e

@app.route('/')
def index():
  return render_template('index.html') #what are we supposed to return???

@app.route('/u/<user_id>', methods=['POST'])
def updateUser(user_id=None):
  client['savethedata']['xxx'].update({
        '_id': user_id,
        'all_challenges.name': request.form['name'],
      },
      {
        '$set': {
          'all_challenges.$.status' : 'complete'
        }
      })
  client['savethedata']['xxx'].update({'_id': user_id},
      {'$inc': {'pts' : 5}})
  return render_template('profile.html', user1=user1)

@app.route('/u/<user_id>', methods=['GET'])
def getUser(user_id=None):
  try:
    user1 = client['savethedata']['xxx'].find_one({"_id": user_id})
    #print user1
    if not user1 or user1== None:
      print "inside for new user"
      user1 = {"_id": user_id,#facebook userid
      "pts": 0, #sum of your completed challenges
      "all_challenges":[{"description": "Raise Awareness by Facebook post!", "pval": 10, "name":"challenge1", "status":"incomplete"},
      {"description": "Read two articles; educate yourself!", "pval": 5, "name":"challenge2","status":"incomplete"},
      {"description": "Raise Awareness", "pval": 10, "name":"challenge3", "status":"incomplete"},
      {"description": "Tweet Out", "pval": 10, "name":"challenge4", "status":"incomplete"},
      {"description": "Write to the FCC", "pval": 15, "name":"challenge5", "status":"incomplete"},
      {"description": "Change Profile Photo", "pval": 5, "name":"challenge6", "status":"incomplete"},
      {"description": "Change Cover Photo", "pval": 5, "name":"challenge7", "status":"incomplete"}],
      "badges":[{"badgeid":"badge1", "tooltiptext":"Successfully Logged In", "badgephoto":"badge1.jpg"},{"badgeid":"badge2", "tooltiptext":"Took First Action", "badgephoto":"badge2.jpg"}
      ,{"badgeid":"badge3", "tooltiptext":"Gained Ten Points", "badgephoto":"badge3.jpg"},{"badgeid":"badge4", "tooltiptext":"Gained 25 Points", "badgephoto":"badge4.jpg"},
      {"badgeid":"badge5", "tooltiptext":"Gained 50 Points", "badgephoto":"badge5.jpg"}]}
      #mongo.db.users.insert(user1)
      client['savethedata']['xxx'].insert(user1)
    return render_template('profile.html', user1=user1)
    #client['savethedata']['xxx'].insert({"user_id": user_id}) //when you go to the profile
  except pymongo.errors.DuplicateKeyError, e:
    print "NOPE"


if __name__ == '__main__':
  #app.debug = True #MUST REMEMBER TO REMOVE LATER
  app.run()
