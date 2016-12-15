import hashlib
salt='cuanljph'

index=1
cache={}

def salted_md5(index):
	def md5(s):
		h=hashlib.md5()
		h.update(s)
		return h.hexdigest()

	def supermd5(s):
		for i in xrange(2017):
			s=md5(s)
		return s
	def calc():
		return supermd5(salt+str(index))
	if (index in cache):
		return cache[index]
	ans=calc()
	cache[index]=ans
	return ans


def enum_seqs(s,n):
	last=None;
	for i,x in enumerate(s):
		if x==last:
			count+=1
			if (count==n):
				yield x
				return
		else:
			last=x
			count=1

def is_good_key(index):
	for x in enum_seqs(salted_md5(index),3):
		for index2 in xrange(index+1,index+1001):
			for y in enum_seqs(salted_md5(index2),5):
				if (y==x):
					return True
	return False

index=-1
good_count=0
while(True):
	index+=1
	if is_good_key(index):
		good_count+=1
		if (good_count==64):
			print index
			exit()
		index+=1