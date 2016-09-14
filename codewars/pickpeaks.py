"""
What is the peak, number have both side number small then them
"""
def pick_peaks(arr):
	sol={"pos":[],"peak":[]}
	if len(arr)<3:
		return sol
	for i in range(1,len(arr)-1):
		if (arr[i-1]< arr[i] )and (arr[i] >= arr[i+1]):
			sol["pos"].append(i)
			sol["peak"].append(arr[i])
	return sol
print(pick_peaks([3,2,3,6,4,1,2,3,2,1,2,3]))
