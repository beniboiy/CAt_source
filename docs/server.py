#!/usr/bin/env python
"""
HTTP Server functioning as middle layer for Slack Integration
__author__ = "Yohan Francis, Ben Robinson"
__copyright__ = ""

__license__ = ""
__version__ = "0.1"
__maintainer__ = "Yohan Francis"
__email__ = "yohan@keaz.co"
__status__ = "Development"
"""
from os import curdir, sep
import BaseHTTPServer
import SocketServer
import requests
import urlparse

PORT = 7888


def slack_login_req(response_url):
    headers = {
                'content-type': 'application/json',
                'Origin': 'http://slackapptest.ddns.net'
                }
    json_payload ={
                        "response_type": "in_channel",
                        "text": "Looks like you need to login",
                        "attachments": [
                            {
                                "text": "<stillfiguringouthowtologin.com>"
                            }
                        ]
                    }
    requests.post(url=response_url, headers=headers, json=json_payload)


class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    # Handler for the GET requests
    def do_GET(self):
        if self.path == "/":
            self.path = "/index.html"
        try:
            # Check the file extension required and
            # set the right mime type
            send_reply = False
            if self.path.endswith(".html"):
                mime_type = 'text/html'
                send_reply = True
            elif self.path.endswith(".png"):
                mime_type = 'image/png'
                send_reply = True
            elif self.path.endswith(".gif"):
                mime_type = 'image/gif'
                send_reply = True
            elif self.path.endswith(".jpg"):
                mime_type = 'image/jpeg'
                send_reply = True
            elif self.path.endswith(".ico"):
                mime_type = 'image/x-icon'
                send_reply = True
            elif self.path.endswith(".js"):
                mime_type = 'application/javascript'
                send_reply = True
            elif self.path.endswith('.txt'):
                mime_type = 'text/*'
                send_reply = True
            elif self.path.endswith(".css"):
                mime_type = 'text/css'
                send_reply = True
            elif self.path.endswith(".otf"):
                mime_type = 'application/vnd.ms-fontobject'
                send_reply = True
            elif self.path.endswith(".ttf"):
                mime_type = 'application/font-sfnt'
                send_reply = True
            else:
                mime_type = False

            if send_reply:
                # Open the static file requested and send it
                f = open(curdir + sep + self.path,'rb')
                self.send_response(200)
                self.send_header('Content-type', mime_type)
                self.send_header('Cache-Control', 'max-age=604800, public')
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
            return

        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)
        return

    def do_HEAD(self):                                              # simple response headers request
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_OPTIONS(self):
        self.send_response(200)                                     # server is not equipped to handle OPTIONS

    def do_POST(self):

        print self.client_address, 'did', self.command               # prints client and request

        try:
            length = int(self.headers.getheader('content-length'))      # gets the length of the content being sent
            field_data = self.rfile.read(length)                        # reads rfile
            fields = urlparse.parse_qs(field_data)
            # parses the contents of rfile and puts it into fields

            print 'fields', fields                      # prints contents of rfile

            try:
                response_url = fields['response_url'][0]
                slack_login_req(response_url=response_url)
                self.send_response(200, 'OK')               # send OK
                self.rfile.write('Debugging: POST OK ')            # send contents
                self.end_headers()                          # end response
                return
            except (ValueError,Exception):
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                filee = open('login.html','rb')
                self.wfile.write(filee.read())

        except (ValueError, TypeError, IOError, Exception), err:
            print err
            self.send_response(400, 'Bad Request')
            self.rfile.write('We could not parse the incoming data', err)


def run(server_class=BaseHTTPServer.HTTPServer,handler_class=MyHandler):
    server_address = ('', PORT)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == '__main__':
    run()
