#!/usr/bin/env python
from webapp2 import RequestHandler

class BoatsHandler(RequestHandler):
    def get(self):
        print("BOATSHANDLER")
        self.response.headers['Content-Type'] = 'text/plain';
        self.response.status_int = 200;
        self.response.out.write('Hello, Boats');

class BoatHandler(RequestHandler):
    def get(self, boat_id):
        print("BoatHandler")
        self.response.headers['Content-Type'] = 'text/plain';
        self.response.status_int = 200;
        self.response.out.write('Hello, Boat ');
        self.response.out.write(boat_id);
