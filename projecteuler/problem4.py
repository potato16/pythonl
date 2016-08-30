palbig=0
for i in range(100,999):
	for j in range(100,999):
		s = str(i*j)
		if s==s[::-1]:
			tmp = int(s)
			if tmp> palbig:
				palbig =tmp
print(palbig)
			

