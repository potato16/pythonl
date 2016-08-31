def checkprime(n):
	i = 2
	while True:
		if n==i:
			return True
		if n%i==0:
			return False
		if i*i>n:
			return True
		i = i+1
	
i = 6
n =14
while True:
	if checkprime(n):
		i = i+1
	if i == 10001:
		print(n)
		break
	n= n+1

