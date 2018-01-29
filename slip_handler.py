#!/usr/bin/env python
from webapp2 import RequestHandler


class SlipsHandler(RequestHandler):
    def get(self):
        print("SlipsHandler")
        self.response.headers['Content-Type'] = 'text/plain';
        self.response.status_int = 200;
        self.response.out.write('Hello, Slips');

class SlipHandler(RequestHandler):
    def get(self, slip_id):
        print("SlipHandler")
        self.response.headers['Content-Type'] = 'text/plain';
        self.response.status_int = 200;
        self.response.out.write('Hello, slip ');
        self.response.out.write(slip_id);
