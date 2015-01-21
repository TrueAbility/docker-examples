#!/usr/bin/python

import SimpleHTTPServer
import SocketServer
import couchdb.client

PORT=80

class Task3Handler(SimpleHTTPServer.SimpleHTTPRequestHandler):
  def do_GET(self):
    try:
      server = couchdb.client.Server(url='http://db:5984/')
      db = server['puzzle']
      image_data = db.get_attachment('3','piece')

    except Exception as err:
      self.send_response(200)
      self.send_header('Content-type','text/html')
      self.end_headers()
      self.wfile.write("<html><body>")
      self.wfile.write("<p>Cannot connect to the database:</p>")
      self.wfile.write("<p>%s</p>" % err)
      self.wfile.write("</body></html>\n")
      return

    if self.path.startswith('/piece'):
      self.send_response(200)
      self.send_header('Content-type','image/png')
      self.end_headers()
      for x in image_data.read():
          self.wfile.write(x)
      return
    else:
      self.send_response(200)
      self.send_header('Content-type','text/html')
      self.end_headers()
      self.wfile.write("<html><body>")
      self.wfile.write("<p>Good job... I can connect to host `db`!</p>")
      self.wfile.write("<p><img src='/piece3.png' /></p>")
      self.wfile.write("<p>You can download this image directly from `/piece3.png`</p>")
      self.wfile.write("</body></html>\n")

httpd = SocketServer.TCPServer(("",PORT), Task3Handler)
httpd.serve_forever()
