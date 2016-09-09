import sys
def reciprocal(d):
	rc =[]
	n=1
	while True:
		n = n*10
		n = n%d
		if n in rc:
			
			return len(rc)-rc.index(n)
		if n ==0:
			return -1
		rc.append(n)

		#break when numberator in list
		#if numberator is not in list then continue
		#if the denominators is bigger then numerator power it with 10

longest =0
for i in range(2,1000):
	tmp = reciprocal(i)
	if tmp>longest:
		longest=tmp
print(longest)
#print(reciprocal(int(sys.argv[1])))

