import re
from collections import defaultdict
def yield_match(regex,input):
	ans=re.search(regex,input)
	if (ans):
		yield ans.groups()
regs=defaultdict(int)
regs['c']=1
inst=[]

for line in open('input12.txt').readlines():
	for src,dst in yield_match('cpy (.*) (.*)',line):
		inst.append(('cpy',src,dst))# copies x (either an integer or the value of a register) into register y.
	for reg, in yield_match('inc (.*)',line):
		inst.append(('inc',reg,'dummy'))# increases the value of register x by one.
	for reg, in yield_match('dec (.*)',line):
		inst.append(('dec',reg,'dummy'))#x decreases the value of register x by one.
	for reg,offset in yield_match('jnz (.*) (.*)',line):
		inst.append(('gnz',reg,int(offset)))#pass# jumps to an instruction y away (positive means forward; 

pc=0
while(pc<len(inst)):
	cur=inst[pc]
	#print pc,cur,regs
	if (cur[0]=='cpy'):
		try:
			src=int(cur[1])
		except ValueError:
			src=regs[cur[1]]
		regs[cur[2]]=src
		pc+=1
		continue
	if (cur[0]=='inc'):
		regs[cur[1]]+=1
		pc+=1
		continue
	if (cur[0]=='dec'):
		regs[cur[1]]-=1
		pc+=1
		continue
	try:
		src=int(cur[1])
	except ValueError:
		src=regs[cur[1]]
	if (src==0):
		pc+=1
	else:
		pc+=cur[2]
print regs['a']