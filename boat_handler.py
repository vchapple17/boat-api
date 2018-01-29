#!/usr/bin/env python
from webapp2 import RequestHandler
import webapp2_extras
import json
from const import baseURL, boatsURL
from Boat import Boat
from google.appengine.ext import ndb


class BoatsHandler(RequestHandler):

    def get(self):
        print("BoatsHandler: GET LIST")
        # Retrieve boats
        boats = Boat.query().fetch()

        # Send response
        res = []
        for boat in boats:
            obj = {
                "url": str(boatsURL + "/" + boat.key.urlsafe()),
                "id": boat.key.urlsafe(),
                "name": boat.name,
                "type": boat.boat_type,
                "length": boat.length,
                "at_sea": boat.at_sea,
            }
            res.append(obj)
        self.response.content_type = 'text/plain'
        self.response.status_int = 200;
        self.response.out.write(json.dumps(res))

    def post(self):
        # Save Request Body
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

        # Create Resource on datastore
        try:
            boat = Boat(name=name, boat_type=boat_type, length=length, at_sea=True);
            boat.put()
        except:
            print()
            self.response.write("Error saving boat");
            self.response.status_int = 400;
            return

        # Send response
        try:
            boat_id = boat.key.urlsafe()
            boatURL = boatsURL + "/" + boat_id;
            self.response.content_type = 'application/json'
            self.response.status_int = 201;
            res = {
                "url": boatURL,
                "id": boat_id,
                "name": boat.name,
                "type": boat.boat_type,
                "length": boat.length,
                "at_sea": boat.at_sea,
            }
            self.response.write(json.dumps(res))
        except:
            self.response.write("Error writing response");
            self.response.status_int = 500;
            return

# Boat identified by id
class BoatHandler(RequestHandler):
    def get(self, boat_id):
        print("BoatHandler: GET 1")

        # Convert boat_id to ndb object
        boat_key = ndb.Key(urlsafe=boat_id);
        boat = boat_key.get()

        # Send response
        boatURL = boatsURL + "/" + boat_id;
        self.response.content_type = 'application/json'
        self.response.status_int = 200;
        res = {
            "url": boatURL,
            "id": boat_id,
            "name": boat.name,
            "type": boat.boat_type,
            "length": boat.length,
            "at_sea": boat.at_sea,
        }
        self.response.write(json.dumps(res))

    def patch(self, boat_id):
        print("BoatHandler: PATCH")