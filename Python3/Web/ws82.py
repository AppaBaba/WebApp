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
        self.wfile.write(bytes("<h1>AppaBaba Home Page</h1>", "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>Hi there from appa.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))
        return

def webserver():
  print('starting server...')

  # Server settings
  host = '127.0.0.1'
  port = 8082
  ws = HTTPServer((host, port), PyhttpRH)
  print('running server...')
  ws.serve_forever()


webserver()
