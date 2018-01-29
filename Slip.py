from google.appengine.ext import ndb

class DepartureHistory(ndb.Model):
    departure_date = ndb.DateProperty()
    departed_boat = ndb.StringProperty()

class Slip(ndb.Model):
    number = ndb.IntegerProperty()
    current_boat = ndb.StringProperty()
    current_boat_url = ndb.StringProperty()
    arrival_date = ndb.DateProperty()
    departure_history = ndb.StructuredProperty(DepartureHistory, repeated=True)
