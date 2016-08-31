f = open('digits.txt')
n =''
while True:
	line = f.readline()
	if len(line)==0:
		break
	n +=line
newstr = n.replace('\n','')
greatest=0
for i in range(len(newstr)-12):
	tmp =newstr[i:i+13]
	g=1
	for i in tmp:
		g = g*int(i)
	if g>greatest:
		greatest = g
print(greatest)
		
