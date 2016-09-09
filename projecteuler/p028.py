from time import time
t= time()
def spiral(n,a,gid):
	s=0
	for i in range(1,gid//2):
		a+=8
		n+=a
		s+=n
	return s

# bottom right
n = 1001
br = spiral(3,2,n)
#bottom left
bl =  spiral(5,4,n)
#top right
tr = spiral(9,8,n)
#top left
tl = spiral(7,6,n)

s= br+bl+tl+tr + 1 + 3 + 5 + 7 + 9
t = time()-t

print(s)
print("{0:.6}s total time.".format(t))
