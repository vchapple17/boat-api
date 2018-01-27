#!/usr/bin/env python
from webapp2 import RequestHandler
import webapp2_extras
import json

from Boat import Boat

from google.appengine.ext import ndb

# class Boat(ndb.Model):
#     name = ndb.StringProperty()
#     boat_type = ndb.StringProperty()
#     length = ndb.IntegerProperty()
#     at_sea = ndb.BooleanProperty()

# https://stackoverflow.com/questions/12664696/how-to-properly-output-json-with-app-engine-python-webapp2

class BoatsHandler(RequestHandler):

    def get(self):
        print("BoatsHandler: GET LIST")
        self.response.headers['Content-Type'] = 'text/plain';
        self.response.status_int = 200;
        self.response.out.write('Hello, List Boats');

    def post(self):
        # Get Request Body
        try:
            req = self.request.body
            obj = json.loads(req)
            name = obj['name'];
            boat_type = obj['type'];
            length = int(obj['length']);

            print("BoatsHandler: POST new boat = " + str(name));
        except (TypeError, ValueError):
            self.response.write("Invalid inputs");
            self.response.status_int = 400;
            return

        # Create Resource Instance
        boat = Boat(name=name, boat_type=boat_type, length=length, at_sea=False);
        boat.put()
        print(boat.key.id)
        # Send response
        self.response.content_type = 'application/json'
        self.response.status_int = 201;
        res = {
            'name': name,
            'type': boat_type,
            'length': length
        }
        self.response.write(json.dumps(res))

# Boat identified by id
class BoatHandler(RequestHandler):
    def get(self, boat_id):
        print("BoatHandler: GET")
        self.response.headers['Content-Type'] = 'text/plain';
        self.response.status_int = 200;
        self.response.out.write('Hello, Boat ');
        self.response.out.write(boat_id);
