data='10011111011011001'
disk_size=272

def expand(a):
	b=a.replace('1','a').replace('0','1').replace('a','0')[::-1]
	return a+'0'+b

def grouper(x):
	it=iter(x)
	for x in it:
		yield x,next(it)
	
def checksum(a):
	if len(a)%2==1:
		return a
	ans=''
	for x,y in grouper(a):
		ans+='1' if x==y else '0'
	return checksum(ans)

while(len(data)<disk_size):
	data=expand(data)

data=data[0:disk_size]
print checksum(data)
