ans=0
for line in open('input3.txt').readlines():
	a,b,c=map(int,filter(None,line.strip().split(' ')))
	if (a+b>c and a+c>b and c+b>a):
		ans+=1
print ans