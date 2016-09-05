import sys
def isabundant(n):
	tmp=0
	for i in range(1,n):
		if n%i==0:
			tmp += i
	if tmp >n:
		return True
	else:
		return False
s =0
ab =[]
for i in range(1,28124):
	s = s+i	
	if isabundant(i):
		ab.append(i)
print(ab)
#print(isabundant(int(sys.argv[1])))
