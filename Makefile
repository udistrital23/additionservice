PACKAGE_NAME=additionservice

build:
	docker build -t $(PACKAGE_NAME) -f Dockerfile .
run:
	docker run -it --rm -p 8001:8001 -v $(shell pwd):/app $(PACKAGE_NAME)

launch:
	FLASK_ENV=development FLASK_APP=src/server.py FLASK_DEBUG=1 python3.8 -m flask run --host=0.0.0.0 --port=8000


