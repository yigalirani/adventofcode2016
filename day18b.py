def get_inputs(row,i):
	row='.'+row+'.'
	ans=row[i:i+3]
	return ans
def calc_is_trap(input):
	return input in ['^^.','.^^','^..','..^']

def calc_next_row(row):
	ans=[]
	for i in xrange(len(row)):
		inputs=get_inputs(row,i)	
		is_trap=calc_is_trap(inputs)
		ans.append('^' if is_trap else '.')
	return ''.join(ans)
row=open('input18.txt').readline().strip()
ans=row.count('.')
for x in xrange(400000-1):
	row=calc_next_row(row)
	ans+=row.count('.')
print ans
