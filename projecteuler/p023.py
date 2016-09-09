import sys
def isabundant(n):
	tmp=0
	st =1
	se =n
	i=st
	while i>= st and i<=se:
		if n%i==0:
			tmp += i + n//i
			st =i
			se =n//i
		i=i+1
	if tmp >n:
		return True
	else:
		return False
s =0
ab =[]
for i in range(1,28124):
	s= s+i
	if isabundant(i):
		ab.append(i)
		print(i)

for i in range(0,len(ab)-1):
	s = s- ab[i]-ab[i+1]
print (s)
#print(isabundant(int(sys.argv[1])))
