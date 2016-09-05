
f= open('p022_names.txt')
names=''
while True:
	line = f.readline()
	if len(line)==0:
		break
	names+=line
f.close()
namel = names.split('"')
for i in namel:
	if i ==',' or i =='':
		namel.remove(i)
namel.sort()
total=0
for i in range(len(namel)):		
	tmp = namel[i]
	if i ==0:
		print(tmp)
	s =0
	for c in tmp:
		s =s + (ord(c)-ord('A'))+1
	if tmp == 'COLIN':
		print ('{},{}={}'.format(s,i,s*i))
	total = total + s*(i+1)	

print(total)
