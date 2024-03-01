#! /usr/bin/env python3

import os
from http.server import HTTPServer, SimpleHTTPRequestHandler

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

IP = '0.0.0.0'
PORT = 8000

class RequestHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE_DIR, **kwargs)


print(f"http://{IP}:{PORT}")
print("Served directory: ", BASE_DIR)
print("ctrl+c to close")

try:
    HTTPServer((IP, PORT), RequestHandler).serve_forever()
except KeyboardInterrupt:
    print("\nServer closed")
