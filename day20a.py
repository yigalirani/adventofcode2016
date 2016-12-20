import re
def yield_match(regex,input):
	ans=re.match(regex,input)
	if (ans):
		yield ans.groups()
cur=[]
def add(start,end):
	for i,(estart,eend) in enumerate(cur):
		if (end+1<estart):
			cur.insert(i,(start,end))
			return
		if (start-1<=eend):
			new=min(start,estart),max(end,eend)
			del cur[i]
			add(*new)
			return
	cur.append((start,end))

for line in open('input20.txt').readlines():
	start,end=map(int,line.strip().split('-'))
	add(start,end)

print cur[0][1]+1
