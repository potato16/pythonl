'''Sum of all primes below two million'''
def isprime(n):
	if n<3:
		return True
	i =2
	while True:
		if n ==i: 
			return True
		if n%i==0:
			return False
		if i*i>n:
			return True
		i = i+1
sop=0
for  i in range (2,2000000):
	if isprime(i):
		sop = sop +i
print(sop)

