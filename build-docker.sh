#!/bin/bash

for d in text-finder text-marker; do
  (cd $d && docker build -t $d .)
done
