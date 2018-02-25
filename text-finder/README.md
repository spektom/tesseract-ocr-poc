text-finder
============

This service finds Chinese and English text in images.

## Building

To build Docker image, run:

    docker build -t text-finder .

## Running

Suppose you have an image file called `text.png` in current directory.
To extract text along with image coordinates around text area, run the following:

    docker run --rm -i -v $(pwd):/data text-finder \
      /data/text.png > info.json

