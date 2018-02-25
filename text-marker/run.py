#!/usr/bin/env python3

import cv2
import sys
import json

cv_img = cv2.imread(sys.argv[1], cv2.IMREAD_UNCHANGED)

for info in json.load(sys.stdin):
  left, top, right, bottom = info["box"]
  cv2.rectangle(cv_img, (left, top), (right, bottom), color=(90,240,60), thickness=2)

cv2.imwrite(sys.argv[2], cv_img)
