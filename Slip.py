from google.appengine.ext import ndb
from datetime import datetime
import json

class DepartureHistory(ndb.Model):
    departure_date = ndb.DateProperty()
    departed_boat = ndb.StringProperty()

class Slip(ndb.Model):
    number = ndb.IntegerProperty()
    current_boat = ndb.StringProperty()
    current_boat_url = ndb.StringProperty()
    arrival_date = ndb.DateProperty()
    departure_history = ndb.StructuredProperty(DepartureHistory, repeated=True)
    # @classmethod
    def _serializeHistory(self):
        # print("_serializeHistory")
        if (len(self.departure_history)) == 0:
            return self.departure_history;
        else:
            ret = []
            for hist in self.departure_history:
                newHist = {
                    "departed_boat": hist.departed_boat,
                    "departure_date": datetime.strftime(hist.departure_date, "%-m/%-d/%Y")
                }
                ret.append(newHist)
            return json.dumps(ret);
