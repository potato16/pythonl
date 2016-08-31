'''Prob 14 : '''
def one23run(n):
	i =1
	while True:
		if n%2==0:
			n = n/2
		else:
			n=3*n+1
		i= i+1
		if n==1:
			return i
	
longest = [0,0]
for i in range(1,1000001):
	distance=one23run(i)
	if distance>longest[1]:
		longest[0]=i
		longest[1]=distance
print(longest)
