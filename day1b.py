import sys
dirs=[(0,1),(1,0),(0,-1),(-1,0)]
locs=set()
x,y,dir=0,0,0
locs.add('0*0')
for i,a in enumerate(open('input1.txt').readline().split(', ')):
	l=int(a[1:])
	dir=(dir+(1 if a[0]=='R' else -1))%4
	d=dirs[dir]
	for step in xrange(l):
		x+=d[0]
		y+=d[1]
		loc=str(x)+'*'+str(y)
		if (loc in locs):
			print abs(x)+abs(y)
			exit()
		locs.add(loc)
	
