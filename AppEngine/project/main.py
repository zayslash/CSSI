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




import logging
import os

import jinja2
import webapp2

import json
import urllib



env = jinja2.Environment(loader=jinja2.FileSystemLoader('template'))


class MainHandler(webapp2.RequestHandler):
    def get(self):




        response = urllib.urlopen("https://uinames.com/api/")
        content = response.read()
        content_dict = json.loads(content)
        logging.info(content_dict)
        main_template = env.get_template('template.html')
        self.response.out.write(main_template.render(content_dict))













class secondHandler(webapp2.RequestHandler):
    def get(self):


        query = self.request.get('q')



        base_url = "http://api.giphy.com/v1/gifs/search?"
        url_params = {'q': 'puppy', 'api_key': 'dc6zaTOxFJmzC', 'limit': 10}
        giphy_response = urllib.urlopen(base_url + urllib.urlencode(url_params)).read()

#        giphy_data_source = urllib.urlopen("http://api.giphy.com/v1/gifs/search?q=food+apples&api_key=dc6zaTOxFJmzC&limit=10")
#        giphy_json_content = giphy_data_source.read()


        parsed_giphy_dictionary = json.loads(giphy_response)
        gif_url = parsed_giphy_dictionary['data'][0]['images']['original']['url']
        template = jinja_environment.get_template('giphy.html')

        self.response.write(template.render({'img_url': gif_url}))








class thirdHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write()




app = webapp2.WSGIApplication(
[
    ('/', MainHandler),
    ('/lol', secondHandler),
    ('/lol2', thirdHandler)

], debug=True)
