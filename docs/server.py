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
from os import curdir, sep          # from OS we're importing the current directory, and separator \
import BaseHTTPServer               # base HTTPServer module
# import SocketServer                  unused import - just in case todo optimize this
import requests                     # python's requests module
import urlparse                     # urlparse is how we grab the fields off requests

PORT = 7888         # server is being run on port 7888 of the machine


def slack_login_req(response_url):
    """
    Incomplete function set up to login users to Slack and authorize using OAuth2
    :param response_url:
    :return:
    """
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
    requests.post(url=response_url, headers=headers, json=json_payload)     # slack login functionality for work


class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):     # main class for the HTTP request handler

    def do_GET(self):
        """
        Handles get requests
        :return:
        """
        if self.path == "/":            # if the request is for home (root)
            self.path = "/index.html"   # direct it to index.html
        try:
            # Check the file extension required and
            # set the right mime type
            # todo refactor into a nice function
            send_reply = False
            # if we can't detect the mimetype we respond with a 501 or something
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
                mime_type = False       # this is mainly here to look pretty

            if send_reply:              # if we found a mimetype
                # Open the static file requested and send it
                f = open(curdir + sep + self.path, 'rb')    # open up the specified file as binary (read)
                self.send_response(200)                     # send 200 OK
                self.send_header('Content-type', mime_type)     # send header specifying content type
                self.send_header('Cache-Control', 'max-age=604800, public')     # send header specifying cache type
                # current cache asks browser to hold for 2 weeks - all data is treated as public
                self.end_headers()                          # end headers
                self.wfile.write(f.read())                  # write the file to the output stream by reading it
                f.close()                                   # close the file
            else:
                self.send_response(501)         # couldn't find mimetype - return 501 status
            return

        except IOError:                         # catch the IOError which means the thing probs doesn't exist
            self.send_error(404, 'File Not Found: %s' % self.path)
        return                                  # this is here to end the req when there's an IOError

    def do_HEAD(self):
        """
        Responds when things ask us for headers.
        :return:
        """
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        return

    def do_OPTIONS(self):
        """
        no
        :return:
        """
        self.send_response(501)                                     # server is not equipped to handle OPTIONS
        # fuck off i don't play with options requests
        return

    def do_POST(self):
        """
        Oh yes the wonderful HTTP post handler.
        :return:
        """
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
