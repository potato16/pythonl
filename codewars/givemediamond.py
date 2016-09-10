def diamond(n):
	array = []
	if type(n)==int and n%2==1 and n>0:
		#make array of string
		hn = n//2
		sc=1
		for i in range(n):
			tmp=''
			
			for x in range(n):
				tmp = ' '*(int((n-sc)/2))+'*'*(sc)+'\n'
			if i<hn:
				sc+=2
			else:
				sc-=2
			array.append(tmp)
		return ''.join(array)
	else:
		return None
print(diamond(55))
