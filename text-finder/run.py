#!/usr/bin/env python3

import tesserocr as tr
import PIL
import sys
import json
import os

LANGUAGES = os.getenv("LANGUAGES", "chi_sim+eng")
CONFIDENCE_MIN = int(os.getenv("CONFIDENCE_MIN", "70"))

with tr.PyTessBaseAPI(lang=LANGUAGES, psm=tr.PSM.SPARSE_TEXT_OSD) as api:

  api.SetImage(PIL.Image.open(sys.argv[1]))
  api.Recognize()
  level = tr.RIL.TEXTLINE
  results = []

  for r in tr.iterate_level(api.GetIterator(), level):
    conf = r.Confidence(level)
    if conf < CONFIDENCE_MIN: continue

    text = r.GetUTF8Text(level).strip()
    if len(text) < 2: continue

    box = r.BoundingBox(level)
    if box is None: continue

    results.append({"conf": conf, "text": text, "box": box})

  print(json.dumps(results, ensure_ascii=False))
