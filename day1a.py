import sys
dirs=[(1,0),(0,-1),(-1,0),(0,1)]
def trim(x):
	if (x==4):
		return 0
	if (x==-1):
		return 3
	return x

with open('input1.txt') as f:
	line=f.readline()
	x,y=0,0
	dir=0
	for a in line.split(', '):
		dir=trim(dir+(1 if a[0]=='L' else -1))
		l=int(a[1:])
		d=dirs[dir]
		x,y=x+d[0]*l,y+d[1]*l
	print abs(x)+abs(y)
