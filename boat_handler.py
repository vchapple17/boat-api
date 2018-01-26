#!/usr/bin/env python
from webapp2 import RequestHandler
import webapp2_extras
import json
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
