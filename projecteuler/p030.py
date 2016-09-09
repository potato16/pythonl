def sumofnum(n):
	n = str(n)
	s=0
	for i in n:
		s+=int(i)**5
	return s
i=2
s=0
while True:
	tmp = sumofnum(i)
	if tmp == i:
		s+=i
		print(s)
	i +=1
