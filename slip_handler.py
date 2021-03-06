#!/usr/bin/env python
from webapp2 import RequestHandler
import webapp2_extras
import json
from const import baseURL, slipsURL
from Slip import Slip
from google.appengine.ext import ndb
from datetime import datetime

class SlipsHandler(RequestHandler):
    def get(self):
        print("SlipsHandler: GET LIST")
        # Retrieve slips
        slips = Slip.query().fetch()

        # Send response
        res = []
        for slip in slips:
            obj = {
                "url": str(slipsURL + "/" + slip.key.urlsafe()),
                "id": slip.key.urlsafe(),
                "number": slip.number,
                "current_boat": slip.current_boat,
                "current_boat_url": slip.current_boat_url
            }
            if (slip.arrival_date) == None:
                obj["arrival_date"] = slip.arrival_date
            else:
                obj["arrival_date"] = datetime.strftime(slip.arrival_date, "%-m/%-d/%Y")
            obj["departure_history"] = slip._serializeHistory()
            res.append(obj)
        self.response.content_type = 'text/plain'
        self.response.status_int = 200;
        self.response.out.write(json.dumps(res))

    def post(self):
        print("SlipsHandler: CREATE SLIP")
        # Save Request Body
        try:
            req = self.request.body
            obj = json.loads(req)

            saveObject = False;     # Update to True if new information given
            for key in obj:
                # Check that key is a valid input
                if (key == "number"):
                    number = int(obj["number"]);
                    saveObject = True;
                else:
                    saveObject = False;
                    # Invalid Information Given in json
                    self.response.write(json.dumps({"error": "Invalid inputs"}));
                    self.response.status_int = 400;
                    return
        except:
            self.response.write(json.dumps({"error": "Invalid inputs"}));
            self.response.status_int = 400;
            return

        # Create Resource on datastore

        try:
            slip = Slip(number=number);
            slip.put()
        except:
            self.response.write(json.dumps({"error": "Error saving Slip"}));
            self.response.status_int = 500;
            return

        # Send response
        try:
            slip_id = slip.key.urlsafe()
            slipURL = slipsURL + "/" + slip_id;
            self.response.content_type = 'application/json'
            self.response.status_int = 201;
            res = {
                "url": slipURL,
                "id": slip_id,
                "number": slip.number,
                "current_boat": slip.current_boat,
                "current_boat_url": slip.current_boat_url,
            }
            if (slip.arrival_date) == None:
                res["arrival_date"] = slip.arrival_date
            else:
                res["arrival_date"] = datetime.strftime(slip.arrival_date, "%-m/%-d/%-Y")

            res["departure_history"] = slip._serializeHistory()

            self.response.write(json.dumps(res))
        except:
            self.response.write(json.dumps({"error": "Error writing response"}));
            self.response.status_int = 500;
            return

class SlipHandler(RequestHandler):
    def get(self, slip_id):
        print("SlipHandler: GET 1")
        # Convert slip_id to ndb object
        try:
            slip_key = ndb.Key(urlsafe=slip_id);
            slip = slip_key.get()
            if (slip == None):
                raise TypeError
        except:
            self.response.write(json.dumps({"error":"Slip not found"}));
            self.response.status_int = 404;
            return

        # Send response
        slipURL = slipsURL + "/" + slip_id;
        self.response.content_type = 'application/json'
        self.response.status_int = 200;
        res = {
            "url": slipURL,
            "id": slip_id,
            "number": slip.number,
            "current_boat": slip.current_boat,
            "current_boat_url": slip.current_boat_url,
        }
        if (slip.arrival_date) == None:
            res["arrival_date"] = slip.arrival_date
        else:
            res["arrival_date"] = datetime.strftime(slip.arrival_date, "%-m/%-d/%Y")

        res["departure_history"] = slip._serializeHistory()

        self.response.write(json.dumps(res))

    def patch(self, slip_id):
        print("SlipHandler: PATCH")

        # Convert slip_id to ndb object
        try:
            slip_key = ndb.Key(urlsafe=slip_id);
            slip = slip_key.get()
            if (slip == None):
                raise TypeError
        except:
            self.response.write(json.dumps({"error": "Invalid Slip ID"}));
            self.response.status_int = 404;
            return

        # Get JSON from Request Body
        try:
            req = self.request.body;
            obj = json.loads(req);
        except:
            self.response.write(json.dumps({"error": "Invalid Request"}));
            self.response.status_int = 400;
            return

        # Iterate through each JSON Key before saving
        try:
            saveObject = False;     # Update to True if new information given
            for key in obj:
                # Check that key is a valid input
                if (key == "number"):
                    slip.number = int(obj["number"]);
                    saveObject = True;
                else:
                    saveObject = False;
                    # Invalid Information Given in JSON
                    self.response.write(json.dumps({"error":"Invalid inputs"}));
                    self.response.status_int = 400;
                    return

        except:
            self.response.write(json.dumps({"error":"Invalid inputs"}));
            self.response.status_int = 400;
            return

        try:
            # Save data if saveObject = True
            if (saveObject == False):
                self.response.write(json.dumps({"error":"Invalid request"}));
                self.response.status_int = 400;
                return
            else:
                slip.put()
        except:
            self.response.write(json.dumps({"error":"Cannot save slip"}));
            self.response.status_int = 500;
            return

        # Send response
        try:
            slip_id = slip.key.urlsafe()
            slipURL = slipsURL + "/" + slip_id;
            self.response.content_type = 'application/json'
            self.response.status_int = 200;
            res = {
                "url": slipURL,
                "id": slip_id,
                "number": slip.number,
                "current_boat": slip.current_boat,
                "current_boat_url": slip.current_boat_url,
                # "arrival_date": slip.arrival_date,
                # "departure_history": str(slip.departure_history)
            }
            if (slip.arrival_date) == None:
                res["arrival_date"] = slip.arrival_date
            else:
                res["arrival_date"] = datetime.strftime(slip.arrival_date, "%-m/%-d/%Y")

            # Stringify departure_history
            res["departure_history"] = slip._serializeHistory()
            self.response.write(json.dumps(res))
        except TypeError:
            self.response.write(json.dumps({"error":"Cannot write response."}));
            self.response.status_int = 500;
            return

    def delete(self, slip_id):
        print("SlipHandler: DELETE 1")

        # Convert slip_id to ndb KEY
        try:
            slip_key = ndb.Key(urlsafe=slip_id);
            slip = slip_key.get();
            if (slip == None):
                raise TypeError
        except:
            self.response.status_int = 204;
            return

        # Release Boat if occupied
        if (slip.current_boat != None):
            # Convert boat_id to ndb objects
            try:
                boat_key = ndb.Key(urlsafe=slip.current_boat);
                boat = boat_key.get();
                if (boat != None):
                    boat.at_sea = True;
                    boat.put();
            except:
                # # Send response that slip is deleted
                self.response.write(json.dumps({"error": "Cannot release boat from slip."}))
                self.response.status_int = 400;
                return
        # Delete ndb entity
        try:
            slip_key.delete();
        except:
            self.response.write(json.dumps({"error": "Error deleting slip"}));
            self.response.status_int = 404;
            return

        # Send response that slip is deleted
        self.response.status_int = 204;
        return;
