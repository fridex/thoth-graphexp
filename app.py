#!/usr/bin/env python3

import os
import http.server
import socketserver

PORT = 8080

Handler = http.server.SimpleHTTPRequestHandler

os.chdir('graphexp/')
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
