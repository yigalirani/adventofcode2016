import re
ans=0
def has_abba(s):
	for i in xrange(len(s)-3):
		if (s[i+0]==s[i+3] and s[i+1]==s[i+2] and s[i+0]!=s[i+1]):
			return True
	return False
for line in open('input7.txt').readlines():
	good=[0,0]
	for i,s in enumerate(re.split('\[|\]',line.strip())):
		if (has_abba(s)):
			good[i%2]+=1
	if (good[0]>0 and good[1]==0):
		ans+=1
print ans

