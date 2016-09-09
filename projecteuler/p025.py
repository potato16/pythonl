f1 =1
f2 =1
i=2
while True:
	tmp = f2
	f2 = tmp +f1
	f1 = tmp
	i =i+1
	if len(str(f2))==1000:
		break
print(i)
