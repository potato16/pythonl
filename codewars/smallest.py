def smallest(n):
	l=[]
	s=n
	itmp = 0
	jtmp = 0
	for  c in str(n):
		l.append(c)
	for i in range(len(l)-1):
		ltmp = l
		d = ltmp.pop(i)
		for j in range(len(ltmp)):
			ltmp.insert(j,d)
			stmp = int(''.join(ltmp))
			if stmp<s:
				s = stmp
				itmp =i
				jtmp =j
				print(stmp)
			else:
				ltmp.pop(j)
	return [s,itmp,jtmp]
print(smallest(261235))		
