board=[[' ']*50 for x in range (6)]
def count_board():
	return sum(row.count('X') for row in board)

def proccess_command(line):
	def decode_command(begin,sep):
		if line.startswith(begin):
			yield map(int,line[len(begin):].split(sep))

	for width,height in decode_command('rect ','x'):
		for y in range(height):
			for x in range(width):
				board[y][x]='X'

	for y,n in decode_command('rotate row y=',' by '):
		row=board[y][:]
		for x in range(50):
			board[y][(x+n)%50]=row[x]

	for x,n in decode_command('rotate column x=',' by '):
		col=[board[y][x] for y in xrange (6)]
		for y in range(6):
			board[(y+n)%6][x]=col[y]

for line in open('input8.txt').readlines():
	proccess_command(line.strip())
print  count_board()
