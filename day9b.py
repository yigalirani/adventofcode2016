line=open('input9.txt').readline().strip()
def calc_decopress_len(start,end):
	if (start==end):
		return 0
	if line[start]=='(':
		pos=line.find(')',start,end)
		if (pos==-1):
			print ("alg too simple to hadle input")
			exit(1)
		n,repeat=map(int,line[start+1:pos].split('x'))
		ans=calc_decopress_len(pos+1,pos+1+n)
		return repeat*ans+calc_decopress_len(pos+1+n,end)
	pos=line.find('(',start,end)
	if (pos==-1):
		return end-start
	return pos-start+calc_decopress_len(pos,end)

print calc_decopress_len(0,len(line))
