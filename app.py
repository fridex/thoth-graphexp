#!/usr/bin/env python3

import os
import http.server
import socketserver

PORT = 8080

# This logic makes JanusGraph host configurable and prevents from submiting internal RH URLs to git repos.
print("Adjusting JanusGraph host")
with open('graphexp/scripts/graphConf.js', 'r') as conf_file:
    lines = conf_file.readlines()

new_lines = []
for line in lines:
    new_lines.append(line.replace('<THOTH_JANUSGRAPH_HOST>', os.environ['THOTH_JANUSGRAPH_HOST']))

with open('graphexp/scripts/graphConf.js', 'w') as conf_file:
    conf_file.write("".join(new_lines))

del lines
del new_lines
del line
del conf_file

os.chdir('graphexp/')

Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
