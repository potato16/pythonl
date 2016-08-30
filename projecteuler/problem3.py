n = 600851475143
ntemp = n
i =2
prime=1
while True:
	if ntemp%i==0:
		ntemp=ntemp/i
		prime = i
	else:
		i=i+1
	if i*i>=n:
		break
print (prime)

