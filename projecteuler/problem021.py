s=0
amicables=[]
for a in range(3,10000):
	if a not in amicables:	
		stmp =0
		for i in range (1,a):
			if a%i==0:
				stmp = stmp + i
		stmp1=0
		for i in range(1,stmp):
			if stmp%i==0:
				stmp1=stmp1+i
		if stmp1 == a and a<stmp:
			s = s+ a+ stmp
			amicables += str(a)
			amicables += str(stmp)
			print('{}={}'.format(a,stmp))
			
print (amicables)
print(s)

