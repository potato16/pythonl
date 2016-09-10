def group_check(s):
	bag =[]
	keys = '(){}[]'
	for c in s:
		if c in keys:
			if len(bag)>0:
				tmp = bag[len(bag)-1]
				if tmp == '(':
					bag.pop() if c==')' else bag.append(c)
				elif tmp == '{':
					bag.pop() if c=='}' else bag.append(c	
				elif tmp == '[':
					bag.pop() if c==']' else bag.append(c	
				else:
					return False
			else:
				bag.append(c)
	return True if len(bag)==0 else False		
