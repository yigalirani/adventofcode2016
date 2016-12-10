import re
from collections import defaultdict
def yield_match(regex,input):
	ans=re.match(regex,input)
	if (ans):
		yield ans.groups()

bots=defaultdict(list)
top_bots=[]
bot_codes={}
def pop_top_bot():
	top_bot=top_bots.pop()
	ans=top_bot,sorted(bots[top_bot])
	del bots[top_bot]
	return ans

def append_to_bot(bot,value):
	bots[bot].append(value)
	if (len(bots[bot])==2):
		top_bots.append(bot)

for line in open('input10.txt').readlines():
	for value,bot in yield_match('value (.*) goes to bot (.*)',line):
		append_to_bot(bot,int(value))
	for line in open('input10.txt').readlines():		
		for bot,low,high in yield_match('bot (.*) gives low to (.*) and high to (.*)',line):
			bot_codes[bot]=(low,high)
ans=1
def generic_append(dest,val):
	global ans
	for outbot, in yield_match('bot (.*)',dest):
		append_to_bot(outbot,val)
	for output, in yield_match('output (.*)',dest):
		if (int(output) in range(3)):
			ans*=val

while(top_bots):
	bot,(low_value,high_value)=pop_top_bot()
	low_dest,high_dest=bot_codes[bot]
	generic_append(low_dest,low_value)
	generic_append(high_dest,high_value)

print ans
