#!/usr/bin/env python

import sys

l=len(sys.argv)
if l > 1:
	for a in sys.argv[1:]:
		print a[::-1]
