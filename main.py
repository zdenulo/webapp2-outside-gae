import webapp2
import jinja2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader('templates'),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class IndexHandler(webapp2.RequestHandler):
    """Basic handler which renders Jinja2 template"""
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render({}))


app = webapp2.WSGIApplication([
    ('/', IndexHandler),
], debug=True)


def main():
    """to run locally"""
    from paste import httpserver
    httpserver.serve(app, host='127.0.0.1')
    app.run()


if __name__ == '__main__':
    main()
