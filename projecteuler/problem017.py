def readit(n):
	book ={ 0:'',1:'one',2: 'two',3: 'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19: 'nineteen',20:'twenty',30:'thirty',40:'fourty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety'}

	if n<21:
		return book[n]
	elif n<100:
		return book[(n//10)*10]+' '+book[n%10]
	elif n<1000:
		tmp = book[n//100]+' hundred '
		s = n%100
		if s>0 and s<21:
			tmp +='and '+book[s]
		elif s>20:
			tmp +='and '+book[(s//10)*10]+' '+book[s%10]
		return tmp
	elif n==1000:
		return 'one thousand'


	

#print(readit(33))
s=''
for i in range(1,1001):
	tmp = readit(i)
	print (tmp)
	s += tmp
s = s.replace(' ','')
print(len(s))
