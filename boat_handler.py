#!/usr/bin/env python
from webapp2 import RequestHandler
import webapp2_extras
import json
from const import baseURL, boatsURL
from Boat import Boat
from Slip import Slip
from google.appengine.ext import ndb
from datetime import datetime
from datetime import date
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
        return

    def post(self):
        print("SlipsHandler: CREATE POST")
        # Save Request Body
        try:
            req = self.request.body
            obj = json.loads(req)
            saveObject = False;     # Update to True if new information given
            for key in obj:
                # Check that key is a valid input
                if (key == "name"):
                    name = obj["name"];
                    saveObject = True;
                elif (key == "type"):
                    boat_type = obj["type"];
                    saveObject = True;
                elif (key == "length"):
                    length = int(obj["length"]);
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
            # Save data only if saveObject = True
            if (saveObject == False):
                self.response.write(json.dumps({"error": "Invalid Request"}));
                self.response.status_int = 400;
                return
            else:
                boat = Boat(name=name, boat_type=boat_type, length=length, at_sea=True);
                boat.put()
        except:
            self.response.write(json.dumps({"error": "Cannot save boat"}));
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
            self.response.write(json.dumps({"error": "Cannot write response."}));
            self.response.status_int = 500;
            return

# Boat identified by id
class BoatHandler(RequestHandler):
    def get(self, boat_id):
        print("BoatHandler: GET 1: " + boat_id)
        # Convert boat_id to ndb object
        try:
            boat_key = ndb.Key(urlsafe=boat_id);
            boat = boat_key.get()
            if (boat == None):
                raise TypeError;
        except:
            self.response.write(json.dumps({"error": "Error getting boat"}));
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

        try:
            # Convert boat_id to ndb object
            boat_key = ndb.Key(urlsafe=boat_id);
            boat = boat_key.get()
            if (boat == None):
                raise TypeError("Boat is of type none")
        except:
            self.response.write(json.dumps({"error": "Invalid Boat ID"}));
            self.response.status_int = 404;
            return;
        # Get json from Request Body
        try:
            req = self.request.body;
            obj = json.loads(req);
        except:
            self.response.write(json.dumps({"error": "Invalid inputs"}));
            self.response.status_int = 400;
            return

        # Iterate through each json Key before saving
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
                    # Invalid Information Given in json
                    self.response.write(json.dumps({"error": "Invalid inputs"}));
                    self.response.status_int = 400;
                    return
        except (TypeError, ValueError):
            self.response.write(json.dumps({"error": "Invalid inputs"}));
            self.response.status_int = 400;
            return

        try:
            # Save data if saveObject = True
            if (saveObject == False):
                self.response.write(json.dumps({"error": "Invalid inputs"}));
                self.response.status_int = 400;
                return
            else:
                boat.put()
        except:
            self.response.write(json.dumps({"error": "Cannot save boat."}));
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
            self.response.write(json.dumps({"error": "Cannot write response"}));
            self.response.status_int = 500;
            return

    def delete(self, boat_id):
        print("BoatHandler: DELETE 1")

        # Convert boat_id to ndb KEY
        try:
            boat_key = ndb.Key(urlsafe=boat_id);
            boat = boat_key.get()
            if (boat == None):
                raise TypeError
        except:
            self.response.status_int = 204;
            return


        # occupied_slip
        try:
            # Find Boat's Slip and Remove
            query = Slip.query()
            slips = query.filter(Slip._properties["current_boat"] == boat_id).fetch()

            if (len(slips) == 1):
                slip = slips[0];

                # Backup Boat URL and ID for Slip
                boatURL = slip.current_boat_url
                boatDate = slip.arrival_date

                # Update Slip
                slip.current_boat = None;
                slip.current_boat_url = None;
                slip.arrival_date = None;

                slip.put()
                print("UPDATED SLIP", slip)
        except:
            # Send Response
            self.response.write(json.dumps({"error": "Cannot update slip."}));
            self.response.status_int = 500;
            return

        # Delete boat entity
        try:
            boat_key.delete();
        except:
            self.response.write(json.dumps({"error": "Cannot delete boat."}));
            self.response.status_int = 404;
            slip.current_boat = boat_id;
            slip.current_boat_url = boatURL;
            slip.arrival_date = boatDate;
            slip.put()
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
            self.response.write(json.dumps({"error": "Invalid inputs"}));
            self.response.status_int = 404;
            return

        try:
            slip_key = ndb.Key(urlsafe=slip_id);
            slip = slip_key.get()
            if (slip == None):
                raise TypeError("Slip is of type none")
        except:
            # print("boat", boat);
            self.response.write(json.dumps({"error": "Invalid inputs"}));
            self.response.status_int = 404;
            return

        # Verify Boat At Sea, reject if not
        if (boat.at_sea == False):
            # print("boat", boat);
            self.response.write(json.dumps({"error": "Boat already docked."}));
            self.response.status_int = 403;
            return

        # Verify Slip Empty, reject if not
        if (slip.current_boat != None) or (slip.current_boat_url != None) or (slip.arrival_date != None):
            # print("slip", slip);
            self.response.write(json.dumps({"error": "Slip already occupied."}));
            self.response.status_int = 403;
            return

        # Get json from Request Body
        try:
            req = self.request.body;
            obj = json.loads(req);
        except:
            self.response.write(json.dumps({"error": "Invalid Request."}));
            self.response.status_int = 400;
            return

        # Iterate through each json Key before saving
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
                    # Invalid Information Given in json
                    self.response.write(json.dumps({"error": "Invalid Request."}));
                    self.response.status_int = 400;
                    return
        except (TypeError, ValueError):
            self.response.write(json.dumps({"error": "Invalid Request."}));
            self.response.status_int = 400;
            return

        # Save new boat info to slip if saveObject = True
        try:
            if (saveObject == False):
                self.response.write(json.dumps({"error": "Invalid Request."}));
                self.response.status_int = 400;
                return
            else:
                slip.current_boat = boat_id
                slip.current_boat_url = boatURL
                slip.put()
        except:
            self.response.write(json.dumps({"error": "Error docking boat."}));
            self.response.status_int = 500;
            return

        # Update Boat.at_sea to be false
        try:
            boat.at_sea = False;
            boat.put();
        except:
            self.response.write(json.dumps({"error": "Error docking boat."}));
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
            self.response.write(json.dumps({"error": "Invalid `departure` parameter"}));
            self.response.status_int = 400;
            return

        # Convert boat_id and slip_id to ndb objects
        try:
            boat_key = ndb.Key(urlsafe=boat_id);
            boat = boat_key.get()
            boatURL = boatsURL + "/" + boat_id;
            if (boat == None):
                raise TypeError
        except:
            self.response.write(json.dumps({"error": "Invalid inputs"}));
            self.response.status_int = 400;
            return

        try:
            slip_key = ndb.Key(urlsafe=slip_id);
            slip = slip_key.get()
            if (slip == None):
                raise TypeError
        except:
            self.response.write(json.dumps({"error": "Invalid inputs"}));
            self.response.status_int = 400;
            return

        # Verify Boat Not At Sea, reject if not
        if (boat.at_sea == True):
            self.response.write(json.dumps({"error": "Boat already at sea"}));
            self.response.status_int = 400;
            return

        # Verify Slip is NOT Empty, reject if not
        if (slip.current_boat == None) and (slip.current_boat_url == None) and (slip.arrival_date == None):
            self.response.write(json.dumps({"error": "Slip already empty"}));
            self.response.status_int = 400;
            return
            #### Cases not tested: when any of the three clauses are None...

        # Update Boat to At Sea
        try:
            boat.at_sea = True;
            boat.put()
        except:
            # print("Cannot update boat");
            self.response.write(json.dumps({"error": "Cannot update boat"}));
            self.response.status_int = 400;
            return

        # Update Slip
        try:
            # Remove current_boat data (boat, url, and arrival date)
            slip.arrival_date = None;
            slip.current_boat = None;
            slip.current_boat_url = None;
            slip.departure_history.append({
                "departure_date": departure_date,
                "departed_boat": boat_id
            })
            slip.put()
            #print("UPDATED SLIP", slip)
        except:
            #print("Cannot update slip");
            # Undo boat update
            boat.at_sea = False;
            boat.put()

            # Send Response
            self.response.write(json.dumps({"error": "Cannot update slip."}));
            self.response.status_int = 400;
            return

        # Send response
        self.response.status_int = 204;
