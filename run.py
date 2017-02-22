#!/usr/bin/python

import facebook
from decouple import config
import sys

FACEBOOK_TOKEN = config('FACEBOOK_TOKEN')
USER_ID = config('USER_ID')
facebook_graph = facebook.GraphAPI(FACEBOOK_TOKEN)
msg = sys.argv


try:
    fb_response = facebook_graph.put_wall_post(msg, profile_id=USER_ID)
    print fb_response
except facebook.GraphAPIError as e:
    print 'Something went wrong:', e.type, e.message
