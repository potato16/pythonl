def countBits(n):
	s=0
	for c in bin(n):
		if c=='1':
			s +=1
	return s
print(countBits(1234))
	
