l=[]
for a in range(2,101):
	for b in range (2,101):
		tmp = a**b
		if tmp not in l:
			l.append(tmp)
print(len(l))
