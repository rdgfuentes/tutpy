#!/usr/bin/env python

import sys

def reverse(s):
	l = len(s)
	r = ''
	while l > 0:
		r += s[l-1]
		l-=1
	return r

l=len(sys.argv)
if l > 1:
	for a in sys.argv[1:]:
		print reverse(a)
