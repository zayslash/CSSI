import logging
import os


import jinja2
import webapp2

env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        main_template = env.get_template('main.html')
        self.response.out.write(main_template.render())
    def post(self):
        results_template = env.get_template('results.html')
        # Note that everything stays the same as the code sample above except
        # this line. We're just swapping out the instruction to print out some
        # text with an instruction to render the results template.
        self.response.out.write(results_template.render())
    # Be sure to leave the "app=" lines that App Engine launcher created in place
    # below this cod
