# Python-Tutorial

Reference: [The Python Tutorial](https://docs.python.org/3/tutorial/index.html)

## Usage

### docker build
docker build -t docker-python3 .

### docker run
docker run --rm -it -v $(pwd):/app docker-python3
or
docker run --rm -it -v $(pwd):/app python:3 python3 /app/app.py
or
docker run --rm -it -v $(pwd):/app python:3 bash