import re
def compare(a,b):
	if (a[1]==b[1]):
		return ord(a[0])-ord(b[0])
	return  b[1]-a[1]

def calc_checksum(s):
	d={}
	for x in s:
		d[x]=d.get(x,0)+1
	l=sorted(list(d.iteritems()),cmp=compare)
	return ''.join([x[0] for x in l])[0:5]

def enum_real_rooms():
	for room in open('input4.txt').readlines():
		a,b=room.split('[')
		checksum=b.strip()[:-1]
		c=a.split('-')
		name=''.join(c[:-1])
		dashed_name='-'.join(c[:-1])
		sector=c[-1]
		calculated_checksum=calc_checksum(name)
		if (checksum==calculated_checksum):
			yield dashed_name,int(sector)
def rotateone(x,n):
	if (x=='-'):
		return' '
	r=ord('z')-ord('a')+1
	return chr((ord(x)-ord('a')+n)%r+ord('a'))
def rotate(name,n):
	return ''.join([rotateone(x,n) for x in name])

for name,sector in enum_real_rooms():
	decrypted_name=rotate(name,sector)
	#print name,rotate(name,sector),sector
	if (re.match('north',decrypted_name)):
		print decrypted_name,sector
