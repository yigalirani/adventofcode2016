import re
ans=0
def enum_aba(s):
	for i in xrange(len(s)-2):
		if (s[i+0]==s[i+2] and s[i+0]!=s[i+1]):
			ans=s[i:i+3]
			yield ans
def supports_ssl(line):
	own=set()
	other=set()
	for i,s in enumerate(re.split('\[|\]',line.strip())):
		own,other=other,own
		for x in enum_aba(s):
			if x[1]+x[0]+x[1] in other:
				return True
			own.add(x)
	return False
ans=0
for line in open('input7.txt').readlines():
	if supports_ssl(line):
		ans+=1
print ans

