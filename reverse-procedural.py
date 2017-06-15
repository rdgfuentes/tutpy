#!/usr/bin/env python

import sys
from lib import string

l=len(sys.argv)
if l > 1:
	for a in sys.argv[1:]:
		print string.lreverse(a)
