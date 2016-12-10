keys=\
['       ',
 '   1   ',
 '  234  ',
 ' 56789 ',
 '  ABC  ',
 '   D   ',
 '       ']	
dirs=dict(L=(-1,0),R=(1,0),U=(0,-1),D=(0,1))
x,y=3,3
for line in open('input2.txt').readlines():
	for c in line.strip():
		dx,dy=dirs[c]
		if (keys[y+dy][x+dx]!=' '):
			x+=dx
			y+=dy
	print keys[y][x],

