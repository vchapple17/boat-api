#!/usr/bin/env python
import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain';
        self.response.status_code = 200
        self.response.out.write('Hello, world')

class BoatsHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain';
        self.response.status_int = 200;
        self.response.out.write('Hello, Boats');
