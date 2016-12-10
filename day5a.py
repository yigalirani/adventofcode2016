import hashlib
def md5(value):
	h=hashlib.md5()
	h.update(value)
	return h.hexdigest()
id='cxdnnyjw'
index=0
ans=''
while(True):
	index+=1
	the_md5=md5(id+str(index))
	if (the_md5[:5]=='00000'):
		ans+=the_md5[5]
		if (len(ans)==8):
			print ans			
			exit()

