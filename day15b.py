#Disc #1 has 17 positions; at time=0, it is at position 5.
import re
from collections import defaultdict
def yield_match(regex,input):
	ans=re.search(regex,input)
	if (ans):
		yield ans.groups()

disks=[]
for line in open('input15.txt').readlines():
	for disk,num_pos,start_pos in yield_match('Disc (.*) has (.*) positions; at time=0, it is at position (.*).',line):
		disks.append((int(num_pos),int(start_pos)))

disks.append((11,0))
def is_good_time(start_time):
	for i,(num_pos,start_pos) in enumerate(disks):
		if (start_time+i+start_pos+1)%num_pos:
			return False
	return True
start_time=0
while(True):
	if (is_good_time(start_time)):
		print start_time
		exit()
	start_time+=1

	
print disks
		