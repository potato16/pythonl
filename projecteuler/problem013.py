'''Problem 013 work out the first ten degits of the sum of the following 
one-hundred 50-digit numbers'''
f = open('prob013.txt')
series =''
s=0
while True:
	line = f.readline()
	if len(line)==0:
		break
	s = s+ int(line.replace('\n',''))	
f.close()
print(str(s)[0:10])
