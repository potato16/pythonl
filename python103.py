def say_hello(name, age):
	print ('He lo >> {}: {} years old'.format(name,age))
def total(a=5,*numbers, **phonebook):
	'''i dont know what is this function about, 
but i can tell you what you reading is useless.'''
	print('a',a)
	for item in numbers:
		print('single_item ',item)
	for mot, hai in phonebook.items():
		print(mot,hai)
say_hello('other guys',78)
print(total(12,3,6,5,4,Thao=393,Su=34123,Canh=132))
print(total.__doc__)
