n = input('Gid nxn: ')
n = int(n)
r =0
def lost(x,y):
	global r
	if x==n and y ==n:	
		r=r+1	
	if x<=n and y<=n:
		lost(x+1,y)
		lost(x,y+1)
lost(0,0)
print(r)
