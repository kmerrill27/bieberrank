#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import jinja2
import os
import webapp2
import time
from google.appengine.ext import ndb

import models


jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class AddBieberHandler(webapp2.RequestHandler):
    """Saves a new Bieber GIF to Datastore to be voted on."""

    def get(self):
        template = jinja_env.get_template('templates/add.html')
        return self.response.write(template.render())

    def post(self):
        title = self.request.get('title')
        image_url = self.request.get('image')

        swag = self.request.get('swag')
        trouble = self.request.get('trouble')
        babybiebs = self.request.get('baby')
        tags = []
        for tag in [swag, trouble, babybiebs]:
          if tag:
            tags.append(tag)

        models.new_image(title, image_url, tags)

        self.redirect('/')


class UpvoteHandler(webapp2.RequestHandler):
    """Registers a vote for a Bieber GIF."""

    def post(self):
        title = self.request.get('title')
        updated_entity = models.upvote(title)


class MainHandler(webapp2.RequestHandler):
    """Displays the top rated Bieber GIFs."""

    def get(self):
        template = jinja_env.get_template('templates/index.html')

        if self.request.get('filter') == 'recent':
          images = models.get_recent()
        elif self.request.get('filter') in ['swag', 'trouble', 'babybiebs']:
          images = models.get_by_tag(self.request.get('filter'))
        else:
          images = models.get_top_ten()

        args = {'images': images }
 
        self.response.write(template.render(args))


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/add', AddBieberHandler),
    ('/upvote', UpvoteHandler)
], debug=True)
