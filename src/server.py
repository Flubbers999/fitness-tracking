# Source - https://stackoverflow.com/a/59102364␍
# Posted by Johnny Abou Haidar, modified by community. See post 'Timeline' for change history␍
# Retrieved 2026-04-14, License - CC BY-SA 4.0␍
#
from http.server import HTTPServer, BaseHTTPRequestHandler
import os


class Serv(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.path = "//src/home.html"
        try:
            print(os.getcwd() + self.path[1:])

            file_to_open = open(os.getcwd() + self.path[1:]).read()
            self.send_response(200)
        except:
            file_to_open = "File not found"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, "utf-8"))


print(os.getcwd())

httpd = HTTPServer(("localhost", 8080), Serv)
httpd.serve_forever()
