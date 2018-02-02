include ../Makefile.common

DIR = /opt/image-to-google-q

.PHONY: all run setup clean

all: setup

FILENAME=images/hello-world.png

run:
	${RUN} bash -c "cd ${DIR} && ./env/bin/python3 main.py ${FILENAME}"

setup:
	${RUN} bash -c "cd ${DIR} && virtualenv -p python3 env"
	${RUN} bash -c "cd ${DIR} && ./env/bin/pip3 install -r requirements.txt"

clean:
	${RUN} bash -c "cd ${DIR} && rm -rf env"
