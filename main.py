import webapp2
class mainPage(webapp2.RequestHandler):
    def get (self):
        self.response.write("Clod Comptinhg")
app=webapp2.WSGIApplication([('/',mainPage)],debug=True)