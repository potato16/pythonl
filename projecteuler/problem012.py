n = 1
i=2
while True:
	n=n+i
	# list the factors
	theguy =1
	bag = []
	while True:
		a= n/theguy
		if a.is_integer():
			bag.append(str(theguy))
			bag.append(str(int(a)))
		theguy = theguy+1
		if str(theguy) in bag:
			break
	if len(bag)>500:
		break
	i=i+1
print(n)
