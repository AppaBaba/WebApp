# Python 3 A Simple Web Server

from http.server import BaseHTTPRequestHandler, HTTPServer

# HTTPRequestHandler class
class PyhttpRH(BaseHTTPRequestHandler):

  # GET
  def do_GET(self):
        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type','text/html')
        self.end_headers()

        # Send message back to client
        message = "Hi there from Appa!"
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return

def webserver():
  print('starting server...')

  # Server settings
  host = '127.0.0.1'
  port = 8081
  ws = HTTPServer((host, port), PyhttpRH)
  print('running server...')
  ws.serve_forever()


webserver()
