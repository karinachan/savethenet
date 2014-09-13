import pymongo

# Connection to Mongo DB
try:
    conn=pymongo.MongoClient('ds035240.mongolab.com:35240/savethedata', 37000)
    db = conn["savethedata"]
    db.authenticate("admin", "catmin")

    print "Connected successfully!!!"
    widgets = db.widgets
    json_data = open("widget.json")
    new_widget = json.load(json_data)
    widgets.insert(new_widget)
except pymongo.errors.ConnectionFailure, e:
   print "Could not connect to MongoDB: %s" % e
conn
