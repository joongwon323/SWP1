from wsgiref.simple_server import make_server
from graph import application

httpd = make_server (
        '10.0.0.1',
         8051,
         application
        )

httpd.serve_forever()
