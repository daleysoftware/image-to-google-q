FROM ubuntu:16.04

RUN apt-get update
RUN apt-get install --yes \
    python3 \
    virtualenv \
    tesseract-ocr

CMD ["sleep", "infinity"]
