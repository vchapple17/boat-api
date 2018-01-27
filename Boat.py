from google.appengine.ext import ndb

class Boat(ndb.Model):
    name = ndb.StringProperty()
    boat_type = ndb.StringProperty()
    length = ndb.IntegerProperty()
    at_sea = ndb.BooleanProperty()
