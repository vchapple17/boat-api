#!/usr/bin/env python

import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain';
        self.response.out.write('Hello, world')

application = webapp2.WSGIApplication([
    ('/', MainPage)
], debug=True)
