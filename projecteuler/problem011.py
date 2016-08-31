f = open('gid.txt')
gid =[]
while True:
	line = f.readline()
	if len(line)==0:
		break
	
	row= line.replace('\n','').split(' ')
#	print (row)
	gid.append(row)	
#print(gid[2][2])
p =0
for x in range(20):
	for y in range(20):
		print(x,y)
		#check diagonally line right
		try:
			print('Ok')
			a=int(gid[x][y])
			b=int(gid[x+1][y+1])
			c=int(gid[x+2][y+2])
			d=int(gid[x+3][y+3])
		except :
			a=1
			b=1
			c=1
			d=1
		tmp=a*b*c*d
		if tmp >p:
			p=tmp
		#check diagonally line left
		try:
			print("2ok")
			a= int(gid[x][y])
			b=int(gid[x+1][y-1])
			c=int(gid[x+2][y-2])
			d=int(gid[x+3][y-3])
		except:
			a=1
			b=1
			c=1
			d=1
		tmp = a*b*c*d
		if tmp>p:
			p=tmp
		#check wasd
		try:
			print("3ok")
			a= int(gid[x][y-1])
			b=int(gid[x][y+1])
			c=int(gid[x-1][y])
			d=int(gid[x+1][y])
		except:
			a=1
			b=1
			c=1
			d=1
		tmp =a*b*c*d
		if tmp>p:
			p = tmp
f.close()
print(p)
