#!/usr/bin/env python

import webapp2
from routes import BoatsHandler, MainPage

application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/boats', BoatsHandler)
], debug=True)
