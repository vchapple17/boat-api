#!/usr/bin/env python
from webapp2 import RequestHandler
import webapp2_extras
import json
from const import baseURL, boatsURL
from Boat import Boat
from google.appengine.ext import ndb
from datetime import datetime

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
        print("SlipsHandler: CREATE POST")
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
        try:
            boat_key = ndb.Key(urlsafe=boat_id);
            boat = boat_key.get()
        except:
            self.response.write({"Error": "Error getting boat"});
            self.response.status_int = 404;
            return

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

        # Convert boat_id to ndb object
        boat_key = ndb.Key(urlsafe=boat_id);
        boat = boat_key.get()

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
                if (key == "name"):
                    boat.name = obj["name"];
                    saveObject = True;
                elif (key == "type"):
                    boat.boat_type = obj["type"];
                    saveObject = True;
                elif (key == "length"):
                    boat.length = int(obj["length"]);
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
                boat.put()
        except:
            self.response.write("Error saving boat");
            self.response.status_int = 400;
            return

        # Send response
        try:
            boat_id = boat.key.urlsafe()
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
        except:
            self.response.write("Error writing response");
            self.response.status_int = 500;
            return

    def delete(self, boat_id):
        print("BoatHandler: DELETE 1")

        # Convert boat_id to ndb KEY
        try:
            boat_key = ndb.Key(urlsafe=boat_id);
        except:
            self.response.write({"Error": "Error getting boat"});
            self.response.status_int = 404;
            return

        # Delete ndb entity
        try:
            boat_key.delete();
        except:
            self.response.write({"Error": "Error deleting boat"});
            self.response.status_int = 404;
            return

        # # Send response that boat is deleted
        self.response.status_int = 204;
        return;


class DockingHandler(RequestHandler):
    def put(self, boat_id, slip_id):
        print("DockingHandler: PUT: Boat to Slip");
        # Add Boat URL, Boat ID, and Arrival Date to Slip

        # Convert boat_id and slip_id to ndb objects
        try:
            boat_key = ndb.Key(urlsafe=boat_id);
            boat = boat_key.get()
            if (boat == None):
                raise TypeError("Boat is of type none")
            boatURL = boatsURL + "/" + boat_id;
        except:
            self.response.write("Invalid Boat ID");
            self.response.status_int = 404;

        try:
            slip_key = ndb.Key(urlsafe=slip_id);
            slip = slip_key.get()
            if (slip == None):
                raise TypeError("Slip is of type none")
        except:
            # print("boat", boat);
            self.response.write("Invalid Slip ID");
            self.response.status_int = 404;
            return

        # Verify Boat At Sea, reject if not
        if (boat.at_sea == False):
            # print("boat", boat);
            self.response.write("Boat already docked.");
            self.response.status_int = 403;
            return

        # Verify Slip Empty, reject if not
        if (slip.current_boat != None) or (slip.current_boat_url != None) or (slip.arrival_date != None):
            # print("slip", slip);
            self.response.write("Slip already occupied.");
            self.response.status_int = 403;
            return

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
                if (key == "arrival_date"):
                    datestring = str(obj["arrival_date"]);
                    slip.arrival_date = datetime.strptime(datestring, "%m/%d/%Y").date();
                    # slip.arrival_date = datestring;
                    saveObject = True;
                else:
                    saveObject = False;
                    # Invalid Information Given in JSON
                    self.response.write("Invalid input(s)");
                    self.response.status_int = 400;
                    return
        except (TypeError, ValueError):
            self.response.write("Invalid JSON input(s)");
            self.response.status_int = 400;
            return

        # Save new boat info to slip if saveObject = True
        try:
            if (saveObject == False):
                self.response.write("Invalid Request");
                self.response.status_int = 400;
                return
            else:
                slip.current_boat = boat_id
                slip.current_boat_url = boatURL
                slip.put()
        except:
            self.response.write("Error docking boat");
            self.response.status_int = 500;
            return

        # Update Boat.at_sea to be false
        try:
            boat.at_sea = False;
            boat.put();
        except:
            self.response.write("Error docking boat");
            self.response.status_int = 500;
            return

        # Send response
        self.response.status_int = 204;


    def delete(self, boat_id, slip_id):
        print("DockingHandler: DELETE: Boat to Sea");

        # Get & Verify Departure Date from Query String
        try:
            dep_date_param = self.request.GET["departure"];
            datestring = str(dep_date_param);
            departure_date = datetime.strptime(datestring, "%m/%d/%Y").date();
        except:
            self.response.write("Invalid `departure` parameter");
            self.response.status_int = 400;

        # Convert boat_id and slip_id to ndb objects
        try:
            boat_key = ndb.Key(urlsafe=boat_id);
            boat = boat_key.get()
            boatURL = boatsURL + "/" + boat_id;
        except:
            self.response.write("Invalid Boat ID");
            self.response.status_int = 400;
        try:
            slip_key = ndb.Key(urlsafe=slip_id);
            slip = slip_key.get()
            if (slip == None):
                raise TypeError
        except:
            self.response.write("Invalid Slip ID");
            self.response.status_int = 400;

        # Verify Boat Not At Sea, reject if not
        if (boat.at_sea == True):
            self.response.write("Boat already at sea.");
            self.response.status_int = 400;
            return

        # Verify Slip is NOT Empty, reject if not
        if (slip.current_boat == None) and (slip.current_boat_url == None) and (slip.arrival_date == None):
            self.response.write("Slip already empty.");
            self.response.status_int = 400;
            return
            #### Cases not tested: when any of the three clauses are None...

        # Update Boat to At Sea
        try:
            boat.at_sea = True;
            boat.put()
        except:
            print("Cannot update boat");
            self.response.write("Cannot update boat.");
            self.response.status_int = 400;
            return

        # Update Slip
        try:
            # add new departure date with boat id
            # slip.departure_history.append(new_departure)
            # print(slip.departure_history);

            # Remove current_boat data (boat, url, and arrival date)
            slip.arrival_date = None;
            slip.current_boat = None;
            slip.current_boat_url = None;
            slip.departure_history.append({
                "departure_date": departure_date,
                "departed_boat": boat_id
            })
            slip.put()
            print("UPDATED SLIP", slip)
        except:
            print("Cannot update slip");
            # Undo boat update
            boat.at_sea = False;
            boat.put()

            # Send Response
            self.response.write("Cannot update slip.");
            self.response.status_int = 400;
            return

        # Send response
        self.response.status_int = 204;
