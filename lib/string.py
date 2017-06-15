
def rreverse(s):
	l = len(s)
	if l <= 1:
		return s
	return s[l-1] + rreverse(s[0:l-1])

def areverse(s):
	r = list(s)
	r.reverse()
	return ''.join(r)

def lreverse(s):
	l = len(s)
	r = ''
	while l > 0:
		r += s[l-1]
		l-=1
	return r