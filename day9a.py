head=0
line=open('input9.txt').readline().strip()
def read_marker(head):
	for i in xrange(head,n):
		if (line[i]==')'):
			marker=line[head+1:i]
			read,repeat=map(int,marker.split('x'))
			return i+1+read,repeat*read
n=len(line)
ans=0
while(head<n):
	c=line[head]
	if c!='(':
		ans+=1
		head+=1
		continue
	head,diff_ans=read_marker(head)
	ans+=diff_ans
print ans


