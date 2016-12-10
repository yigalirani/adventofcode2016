from collections import Counter
d=[]
for line in file('input6.txt').readlines():
	for i,x in enumerate(line):
		if (len(d)<=i):
			d.append(Counter())
		d[i][x]+=1
def most_freq(x):
	return min(x.iterkeys(), key=(lambda key: x[key]))
print ''.join([most_freq(x) for x in d])