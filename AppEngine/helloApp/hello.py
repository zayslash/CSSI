import webapp2
import jinja2

JINJA_ENV = jinja2.Environment( loader= jinja2.FileSystemLoader("Templates") )

html_page= """
<html>
      <head>
            <title> Hello </title>
      </head>
      <body>
            <p> Hello Brooklyn, CSSI! </p>
     </body>
</html>
"""

html_page2= """
<html>
   <body>
     <form action= "/" method="post">
     Name: <input type="text" name="field1"/>
     <input type="submit" value="Submit"/>
     </form>
</body>
</html>
"""


class MainHandler(webapp2.RequestHandler):
    def get(self):
     self.response.write(html_page2)
    def post(self):
        self.response.headers['Content-Type'] = 'text/plain'
        #self.response.write(self.request.POST)
        if "field1" not in self.request.POST:
            self.response.write('field1 not found')
        else:
            field1 = self.request.POST['field1']
            self.response.write("hello " + field1 + "!")

class AboutHandler (webapp2.RequestHandler):
    def get(self):
        self.response.write("all about about")
class GreetingHandler (webapp2.RequestHandler):
    def get(self):
        #self.response.write("booooooo, im casper")
        template_values= {"name":"brooklyn"}
        template = JINJA_ENV.get_template('index.html')
        self.response.write(template.render(template_values))


app = webapp2.WSGIApplication([
      ('/', MainHandler),
      ('/about', AboutHandler),
      ('/howdy',GreetingHandler)
 ], debug= True)
