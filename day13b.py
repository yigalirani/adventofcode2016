from collections import deque
def graph_search(start_state,enum_neigboors,target_steps):
	visited=set()
	visited.add(start_state)
	queue=deque()
	queue.append((start_state,0))
	while(True):
		current,cost=queue.popleft()
		if (cost==target_steps):
				return len(visited)
		for x in enum_neigboors(current):
	
			if (x not in visited):
				visited.add(x)
				queue.append((x,cost+1))

def enum_next(x,y):
	for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
		if (x+dx>=0 and y+dy>=0):
			yield (x+dx,y+dy)
def is_open(x,y):
	return bin(x*x + 3*x + 2*x*y + y + y*y+1350).count('1')%2==0

def get_next(loc):
	x,y=map(int,loc.split(','))
	#print x,y
	for x2,y2 in enum_next(x,y):
		if is_open(x2,y2):
			yield str(x2)+','+str(y2)	
print graph_search('1,1',get_next,50)
