from collections import deque
import hashlib
salt='dmypynyp'
def md5(s):
	h=hashlib.md5()
	h.update(s)
	return h.hexdigest()

def graph_search(start_state,enum_neigboors,is_goal):
	visited=set()
	visited.add(start_state)
	queue=deque()
	queue.append((start_state,0))
	while(True):
		current,cost=queue.popleft()
		if (is_goal(current)):
				return current
		for x in enum_neigboors(current):
			if (x not in visited):
				visited.add(x)
				queue.append((x,cost+1))
def path_to_loc(path):
	x=0
	y=0
	dirs=dict(U=(0,-1),D=(0,1),L=(-1,0),R=(1,0))
	for d in path:
		dx,dy=dirs[d]
		x+=dx
		y+=dy
	return x,y

def valid(x):
	return x>=0 and x<=3

def get_next(p):
	def is_open(x):
		return x in "bcdeorf"
	m=md5(salt+p)[:4]
	allowed=map(is_open,m)
	ans=[]
	for allowed,code in zip(allowed,list('UDLR')):
		if (allowed):
			ans.append(code)
			newpath=p+code
			loc=path_to_loc(newpath)
			if (valid(loc[0]) and valid(loc[1])):
				yield newpath
		

def is_goal(path):
	return path_to_loc(path)==(3,3)
print graph_search('',get_next,is_goal)
	