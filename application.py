from flask import Flask
from flask import render_template
from flask import request
import pymongo
import sys, os
import datetime
from pymongo import MongoClient
app = Flask(__name__)

#connect to MongoDB with the defaults 
mongo = PyMongo(app)

@app.route('/')
def index():
  return url_for('static', filename='index.html') #what are we supposed to return???


@app.route('/u/<user_id>/')
def profile(user_id=None):
  #shows the profile page for one user
  return render_template('profile.html', user_id=user_id)

@app.route('/u/<user_id>/', method=['POST'])
def updateUser(user_id=None):
  user = request.args.get('key', '') #gets username from url 
  user_prof = mongo.db.users.find_one({'_id', user}) 
  if user_prof:
    #update the user
  else: 
    #this is an error
    pass 
  return render_template('profile.html', user_id=user_id)

@app.route('/u/<user_id>/', method=['GET'])
def getUser(user_id=None):
  try:
    user1 = mongo.db.users.find_one({"_id": user_id})
    if not user1: 
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
      mongo.db.users.insert(user1)
    #client['savethedata']['xxx'].insert({"user_id": user_id}) //when you go to the profile
  except pymongo.errors.DuplicateKeyError, e:
    print "NOPE"
  return render_template('profile.html', user1=user1)


@app.route('/bye/')
def logout():
  return 'Logout Page'

if __name__ == '__main__':
  app.debug = True #MUST REMEMBER TO REMOVE LATER
  app.run()