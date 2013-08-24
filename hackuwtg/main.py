import os
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb
from google.appengine.ext import db

import jinja2
import webapp2
import json

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'])


class MainPage(webapp2.RequestHandler):
	def get(self):
		self.response.write("Hello Kasab!")

application = webapp2.WSGIApplication([
    ('/', MainPage)
], debug=True)
