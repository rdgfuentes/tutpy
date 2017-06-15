#!/usr/bin/env python

import sys

def reverse(s):
	r = list(s)
	r.reverse()
	return ''.join(r)


l=len(sys.argv)
if l > 1:
	for a in sys.argv[1:]:
		print reverse(a)
