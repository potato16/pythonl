a = 100
k = 10
modulo = 1000000007
n = 1
for i in range (1,101):
	n=n*i
i=2
d =[]
while True:
	if n%i ==0:
		d.append(i)
		n = n/i
		print(i)
	else:
		i+=1
	#tam
	if i>n: 
		break
print(d)
