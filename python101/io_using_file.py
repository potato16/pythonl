poem = '''\
Rose are red,
Violet are blue
I cant write it anymore,
Because it's so Mooo!
'''
#Open for 'w'riting
f = open('poem.txt','w')
f.write(poem)
f.close
f=open('poem.txt')
while True:
	line = f.readline()
	if len(line) ==0:
		break
	print(line,end='')
f.close
