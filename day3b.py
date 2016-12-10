def enum_triangles():
	a=map(int,filter(None,open('input3.txt').read().replace('\n','').split(' ')))
	for i in xrange(0,len(a),9):
		for j in xrange(0,3):
			yield a[i+j],a[i+j+3],a[i+j+6]

ans=0
for a,b,c in enum_triangles():
	if (a+b>c and a+c>b and c+b>a):
		ans+=1
print ans