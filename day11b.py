import re
from collections import deque
def yield_match(regex,input):
	ans=re.search(regex,input)
	if (ans):
		yield ans.groups()

def read_state_from_file():
	materials=[]
	def get_index(name):
		if name not in materials:
			materials.append(name)
			return len(materials)-1
		return materials.index(name)
	
	def translate(content):
		microchips=[' ']*7
		generators=[' ']*7
		for x in content.split(','):
			for y, in yield_match('a (.*)-compatible microchip',x):
				microchips[get_index(y)]='m'
			for y, in yield_match('a (.*) generator',x):
				generators[get_index(y)]='g'
		return ''.join(microchips)+''.join(generators)

	ans=[]
	for line in open('input11.txt').readlines():
		for floor,content in yield_match('The (.*) floor contains (.*)',line):
			floor='first,second,third,fourth'.split(',').index(floor)
			ans.append(translate(content))

	ans[0]=ans[0][0:5]+'mm'+ans[0][7:12]+'gg'
	return '\n'.join(ans)+'-0'

def is_valid_floor(floor):
	has_genrators=floor.count('g')>=1
	if (not has_genrators):
		return True
	for i,x in enumerate(floor[0:5]):
		if (x=='m' and floor[5+i]!='g' and has_genrators):
			return False
	return True

def enum_make_state(floors,new_elevator,elevator,i,j):
	new_floor=list(floors[new_elevator])
	new_floor[i]=floors[elevator][i]
	new_floor[j]=floors[elevator][j]
	new_floor=''.join(new_floor)
	old_floor=list(floors[elevator])
	old_floor[i]=' '
	old_floor[j]=' '
	old_floor=''.join(old_floor)
	if not is_valid_floor(old_floor) or not is_valid_floor(new_floor):
		return
	ans=[]
	for i in xrange(4):
		if (i==new_elevator):
			ans.append(new_floor)
			continue
		if (i==elevator):
			ans.append(old_floor)
			continue
		ans.append(floors[i])
	yield '\n'.join(ans)+'-'+str(new_elevator)

def enum_states(s):
	floors,elevator=s.split('-')
	floors=floors.split('\n')
	elevator=int(elevator)
	for new_elevator in (elevator-1,elevator+1):
		if (new_elevator==-1 or new_elevator==4):
			continue
		for i,x in enumerate(floors[elevator]):
			if (x!=' '):
				for j,y in enumerate(floors[elevator]):	
					if (i>=j and y!=' '):
						for new_state in enum_make_state(floors,new_elevator,elevator,i,j):
							yield new_state

def is_valid_floor(floor):
	has_genrators=floor.count('g')>=1
	if (not has_genrators):
		return True
	for i,x in enumerate(floor[0:7]):
		if (x=='m' and floor[7+i]!='g' and has_genrators):
			return False
	return True

def graph_search(start_state,end_state,enum_neigboors):
	visited=set()
	visited.add(start_state)
	queue=deque()
	queue.append((start_state,0))
	while(True):
		current,cost=queue.popleft()
		for x in enum_neigboors(current):
			if (x==end_state):
				return cost
			if (x not in visited):
				visited.add(x)
				queue.append((x,cost+1))


def runit():
	read_state=read_state_from_file()
	end_state=(' '*14+'\n')*3+'mmmmmmmggggggg-3'
	print graph_search(read_state,end_state,enum_states)

runit()
