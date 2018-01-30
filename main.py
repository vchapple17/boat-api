#!/usr/bin/env python

import webapp2
from webapp2 import Route
from boat_handler import BoatsHandler, BoatHandler, DockingHandler
from slip_handler import SlipsHandler, SlipHandler
from webapp2_extras.routes import RedirectRoute, PathPrefixRoute

DEBUG_FLAG = True

# Monkey Patch for webapp2 PATCH
#https://stackoverflow.com/questions/16280496/patch-method-handler-on-google-appengine-webapp2

allowed_methods = webapp2.WSGIApplication.allowed_methods
new_allowed_methods = allowed_methods.union(('PATCH',))
webapp2.WSGIApplication.allowed_methods = new_allowed_methods


application = webapp2.WSGIApplication([

    Route('/boats', handler=BoatsHandler, name='boats'),
    PathPrefixRoute( '/boats',[
        Route('/', handler=BoatsHandler, name='boats'),
        Route('/<boat_id:([A-Z]|[a-z]|[0-9]|[-])+(/)?>', handler=BoatHandler, name='boat'),
        Route('/<boat_id:([A-Z]|[a-z]|[0-9]|[-])+>/slips/<slip_id:([A-Z]|[a-z]|[0-9]|[-])+(/)?>', handler=DockingHandler, name='docking'),

    ]),

    Route('/slips', handler=SlipsHandler, name='slips'),
    PathPrefixRoute( '/slips',[
        Route('/', handler=SlipsHandler, name='slips'),
        Route('/<slip_id:([A-Z]|[a-z]|[0-9]|[-])+(/)?>', handler=SlipHandler, name='slip'),
    ]),

], debug=DEBUG_FLAG)
