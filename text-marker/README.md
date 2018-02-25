text-marker
===========

This service marks text in images based on info produced by the `text-finder` service.

## Building

To build Docker image, run:

    docker build -t text-marker .

## Running

Suppose you have an image file called `text.png` in current directory.
To produce marked image, run the following command:

    docker run --rm -i -v $(pwd):/data text-marker \
      /data/text.png /data/text_marked.png < info.json

