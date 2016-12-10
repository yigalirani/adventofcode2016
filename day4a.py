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

ans=0
for room in open('input4.txt').readlines():
	a,b=room.split('[')
	checksum=b.strip()[:-1]
	c=a.split('-')
	name=''.join(c[:-1]).replace('-','')
	sector=c[-1]
	calculated_checksum=calc_checksum(name)
	if (checksum==calculated_checksum):
		ans+=int(sector)
print ans
