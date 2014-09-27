import os
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb

import jinja2
import webapp2


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
# [END imports]


# [START main_page]
class MainPage(webapp2.RequestHandler):

    def get(self):
        template_values = {
            'id': 1,
            'name': "Teresa"
        }

        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))
# [END main_page]


application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)