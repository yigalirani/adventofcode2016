def valid(x):
	return x>=0 and x<=2
keys=['123','456','789']
dirs=dict(L=(-1,0),R=(1,0),U=(0,-1),D=(0,1))
x,y=1,1
for line in open('input2.txt').readlines():
	for c in line.strip():
		dx,dy=dirs[c]
		if (valid(x+dx) and valid(y+dy)):
			x+=dx
			y+=dy
	print keys[y][x],

