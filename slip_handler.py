#!/usr/bin/env python
from webapp2 import RequestHandler
import webapp2_extras
import json
from const import baseURL, slipsURL
from Slip import Slip
from google.appengine.ext import ndb


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
                "current_boat_url": slip.current_boat_url,
                "arrival_date": slip.arrival_date,
                "departure_history": slip.departure_history
            }
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
            number = obj['number'];
            print("SlipsHandler: POST new slip #" + str(number));
        except (TypeError, ValueError):
            self.response.write("Invalid inputs");
            self.response.status_int = 400;
            return

        # Create Resource on datastore
        try:
            slip = Slip(number=number);
            slip.put()
        except:
            self.response.write("Error saving Slip");
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
                "arrival_date": slip.arrival_date,
                "departure_history": slip.departure_history
            }
            self.response.write(json.dumps(res))
        except:
            self.response.write("Error writing response");
            self.response.status_int = 500;
            return


class SlipHandler(RequestHandler):
    def get(self, slip_id):
        print("SlipHandler: GET 1")
        # Convert slip_id to ndb object
        try:
            slip_key = ndb.Key(urlsafe=slip_id);
            slip = slip_key.get()
        except:
            self.response.write({"Error": "Error getting slip"});
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
            "arrival_date": slip.arrival_date,
            "departure_history": slip.departure_history
        }
        self.response.write(json.dumps(res))

    def patch(self, slip_id):
        print("SlipHandler: PATCH")

        # Convert slip_id to ndb object
        slip_key = ndb.Key(urlsafe=slip_id);
        slip = slip_key.get()

        # Get JSON from Request Body
        try:
            req = self.request.body;
            obj = json.loads(req);
        except:
            self.response.write("No JSON body in Request");
            self.response.status_int = 400;
            return

        # Iterate through each JSON Key before saving
        try:
            saveObject = False;     # Update to True if new information given
            for key in obj:
                # Check that key is a valid input
                if (key == "number"):
                    slip.number = obj["number"];
                    saveObject = True;
                else:
                    saveObject = False;
                    # Invalid Information Given in JSON
                    self.response.write("Invalid inputs");
                    self.response.status_int = 400;
                    return

        except (TypeError, ValueError):
            self.response.write("Invalid inputs");
            self.response.status_int = 400;
            return

        try:
            # Save data if saveObject = True
            if (saveObject == False):
                self.response.write("Invalid Request");
                self.response.status_int = 400;
                return
            else:
                print("SAVE SLIP: ", slip)
                slip.put()
        except:
            self.response.write("Error saving slip");
            self.response.status_int = 400;
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
                "arrival_date": slip.arrival_date,
                "departure_history": slip.departure_history
            }
            self.response.write(json.dumps(res))
        except:
            self.response.write("Error writing response");
            self.response.status_int = 500;
            return


    def delete(self, slip_id):
        print("SlipHandler: DELETE 1")

        # Convert slip_id to ndb KEY
        try:
            slip_key = ndb.Key(urlsafe=slip_id);
        except:
            self.response.write({"Error": "Error getting slip"});
            self.response.status_int = 404;
            return

        # Delete ndb entity
        try:
            slip_key.delete();
        except:
            self.response.write({"Error": "Error deleting slip"});
            self.response.status_int = 404;
            return

        # # Send response that slip is deleted
        self.response.status_int = 204;
        return;
