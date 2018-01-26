#!/usr/bin/env python

import webapp2
from webapp2 import Route
from boat_handler import BoatsHandler, BoatHandler
from slip_handler import SlipsHandler, SlipHandler
from webapp2_extras import routes

DEBUG_FLAG = True

application = webapp2.WSGIApplication([
    # Route(r'/', handler=MainPage, name='home'),
    routes.PathPrefixRoute( r'/boats',[
        Route(r'/', handler=BoatsHandler, name='boats'),
        Route('/<boat_id:\w+>', handler=BoatHandler, name='boat'),
    ]),
    routes.PathPrefixRoute( r'/slips',[
        Route(r'/', handler=SlipsHandler, name='slips'),
        Route('/<slip_id:\w+>', handler=SlipHandler, name='slip'),
    ]),
], debug=DEBUG_FLAG)
