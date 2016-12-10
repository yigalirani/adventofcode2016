import hashlib
def md5(value):
	h=hashlib.md5()
	h.update(value)
	return h.hexdigest()
def hex_to_num(x):
	return ord(x)-ord('a')
id='cxdnnyjw'
index=0
ans=['_']*8
count=0
while(True):
	index+=1
	the_md5=md5(id+str(index))
	if (the_md5[:5]=='00000'):
		pos,value=list(the_md5[5:7])
		pos=ord(pos)-ord('0')
		if (pos<8 and ans[pos]=='_'):
			ans[pos]=value
			count+=1			
			if (count==8):
				print ''.join(ans)
				exit()

