ring_size=3001330
elf=[1]*ring_size
cur=0
def get_next_elf(cur):
	while True:
		cur=(cur+1)%ring_size
		if elf[cur]:
			return cur
while(True):
	take_from=get_next_elf(cur)
	elf[cur]+=elf[take_from]
	elf[take_from]=0
	if elf[cur]==ring_size:
		print cur+1
		exit()
	cur=get_next_elf(cur)
		
	