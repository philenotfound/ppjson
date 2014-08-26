#!/usr/bin/python
# -*- coding: utf-8 -*-
# (c) 2014, Phil Eichinger, phil@zankapfel.net
# License: GPLv2
#
# Pretty print JSON objects, either from file or stdin
import json
import sys

if( len(sys.argv) == 1 ):
  j = json.load(sys.stdin)
else:
  f = open( sys.argv[1], "r")
  j = json.load(f)
  f.close()

print( json.dumps( j,sort_keys=True,indent=4, separators=(',', ': ')) )

