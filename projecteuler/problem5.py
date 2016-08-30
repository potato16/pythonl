
ml = []
#init array
for i in range(1,21):
	ml.append(i)
#cal array
for i in range (0,20):
	for j in range(i+1,20):

		if ml[j]%ml[i]==0:
			ml[j]=ml[j]/ml[i]
# output
output =1
for i in range(0,20):
	output= output*ml[i]
print(int(output))

