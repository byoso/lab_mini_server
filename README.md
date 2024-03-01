

This contenairized server can be usefull to try things (e.g: trying to work with varnish)

# Structure of the project

```sh
.
├── Dockerfile
├── Makefile
└── server
    ├── mini_server.py
    ├── ott_1
    │   └── Ott_1
    ├── ott_2
    │   └── Ott_2
    └── ott_3
        └── Ott_3

```

# files

**mini_server.py**
```python
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
```

**Dockerfile**
```sh
FROM python:3.9.18-alpine3.19

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1

COPY . /app

WORKDIR /app/server

EXPOSE 8000

CMD ["python3", "mini_server.py"]

```

**Makefile**
```sh
run:
	docker build . -t lab_mini_server
	docker run -p 8000:8000 --name lab_mini_server lab_mini_server
	##########################

stop:
	docker stop lab_mini_server
	docker rm lab_mini_server
	##########################

it:
	docker exec -it lab_mini_server /bin/sh
	##########################

clean:
	docker rmi lab_mini_server
	##########################
```

**server/**

The directories and files in server/ are empty, it is just to provide something to serve.
