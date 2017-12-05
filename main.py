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
import os
import jinja2
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('index.html')
    	title = "Event Seeker | Find Your Events"
        navText =  "CREATE EVENT"
        navHref = "create_event.html"
        navIcon = "glyphicon glyphicon-plus" # glyphicon glyphicon-eye-open
    	template_vars = {
    		'title' : title,
            'navText' : navText,
            'navHref':  navHref,
            'navIcon' : navIcon
    	}
        self.response.out.write(template.render(template_vars))

class aboutHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('about.html')
    	title = "Event Seeker | About Us"
        navText =  "CREATE EVENT"
        navHref = "create_event.html"
        navIcon = "glyphicon glyphicon-plus" # glyphicon glyphicon-eye-open
    	template_vars = {
    		'title' : title,
            'navText' : navText,
            'navHref':  navHref,
            'navIcon' : navIcon
    	}
        self.response.out.write(template.render(template_vars))

class createHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('create_event.html')
        title = "Event Seeker | Create an Event"
        createStyle = "css/create_event.css"
        navText =  "BROWSE EVENT"
        navHref = "index.html"
        navIcon = "glyphicon glyphicon-eye-open" # glyphicon glyphicon-eye-open
    	template_vars = {
    		'title' : title,
            'createStyle' : createStyle,
            'navText' : navText,
            'navHref':  navHref,
            'navIcon' : navIcon
    	}
        self.response.out.write(template.render(template_vars))

class eventIntroHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('eventintro.html')
    	title = "Event Seeker | Event Details"
        navText =  "CREATE EVENT"
        navHref = "index.html"
        navIcon = "glyphicon glyphicon-plus"
    	template_vars = {
    		'title' : title,
            'navText' : navText,
            'navHref':  navHref,
            'navIcon' : navIcon
    	}
        self.response.out.write(template.render(template_vars))

class loginHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('login.html')
        title = "Event Seeker | Login"
        createStyle = "css/login.css"
        navText =  " CREATE EVENT"
        navHref = "create_event.html"
        navIcon = "glyphicon glyphicon-plus" # glyphicon glyphicon-eye-open
    	template_vars = {
    		'title' : title,
            'createStyle' : createStyle,
            'navText' : navText,
            'navHref':  navHref,
            'navIcon' : navIcon
    	}
        self.response.out.write(template.render(template_vars))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/index.html', MainHandler),
    ('/about.html', aboutHandler),
    ('/create_event.html', createHandler),
    ('/eventintro.html', eventIntroHandler),
    ('/login.html', loginHandler)
], debug=True)
