#!/usr/bin/env python

import sys

def reverse(s):
	l = len(s)
	if l <= 1:
		return s

	return s[l-1] + reverse(s[0:l-1])


l=len(sys.argv)
if l > 1:
	for a in sys.argv[1:]:
		print reverse(a)
