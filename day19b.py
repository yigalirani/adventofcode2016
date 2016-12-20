ring_size=3001330
elf=[1]*ring_size
cur=0

cur_across=ring_size/2


def get_next_elf(cur):
	while True:
		cur=(cur+1)%ring_size
		if elf[cur]:
			return cur
extra_jump=ring_size%2


while(True):  
	if cur==cur_across:
		print 'alg bug'
	elf[cur]+=elf[cur_across]
	elf[cur_across]=0

	if elf[cur]==ring_size:
		print cur+1
		exit()
	cur_across=get_next_elf(cur_across)
	if extra_jump:
		cur_across=get_next_elf(cur_across)
	extra_jump=(extra_jump+1)%2
	cur=get_next_elf(cur)
