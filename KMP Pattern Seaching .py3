# LPS -> It indicates longest proper prefix which is also proper suffix
# Proper Prefix of 'ABC' is 'A' and 'AB' but not 'ABC'
# Proper Suffix of 'ABC' is 'C' and 'BC' but not 'ABC'
# So for string 'ABCABD' the LPS Array should be [0,0,0,1,2,0]

# Why?
# LPS[0] is always be 0 because its the first element
# LPS[1] is 0 because pat[1] not match with pat[0]
# LPS[2] is 0 because pat[2] not match with par[0]
# LPS[3] is 1 beacase pat[3] match with pat[0] and now we check for pat[1]
# LPS[4] is 2 beacase pat[4] match with pat[1] and now we check for pat[2]
# LPS[5] is 0 beacase pat[5] match with pat[2] and also not match with pat[0].

def computeLPS(pat):
	M = len(pat)
	LPS = [0]*M
	l = 0
	i = 1

	while i<M:
		if pat[i] == pat[l]:
			l += 1
			LPS[i] = l
			i += 1
		else:
			if l != 0:
				l = LPS[l-1]
			else:
				LPS[i] = 0
				i += 1
	return LPS

def KMP(txt, pat):
	M = len(pat)
	N = len(txt)

	LPS = computeLPS(pat)
	i,j = 0,0

	while i<N:

		if pat[j] == txt[i]: # if character match
			i += 1
			j += 1
		if j == M: 			 # if all character match
			yield i-j
			j = LPS[j-1]

		elif i < N and pat[j] != txt[i]: # if character not match
			if j != 0:
				j = LPS[j-1]
			else:
				i += 1

txt = 'JDABDFJLKASBFBASDBABDFJKABJGKFABFFL'
pat = 'AB'

for i in KMP(txt,pat):
	print('pattern found at %s index of txt'%i)

#or do list( KM(txt,pat) ) to get result in form of list.
