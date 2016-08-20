import sys
if(sys.argv[1]=='0'):
	
	#list
	listhang=['con chuot','may tinh', 'loa']
	print('I have {} items to purchase.'.format(len(listhang)))
	print('These items are:', end=' ')
	for item in listhang:
		print(item, end=' ')
	print('\nI also have to buy VGA.')
	listhang.append('VGA DONGKING')
	print('My list hang is ',listhang)
	print('I will sort my list now')
	listhang.sort()
	print('Sorted list is: ', listhang)
	print('The first item i will buy is ', listhang[0])
	olditem = listhang[0]
	del listhang[0]
	print('I bought the ', olditem)
	print ('My list hang is now', listhang)
elif(sys.argv[1]=='1'):

	#Tuple
	person=('Hateful', 'Rat', 'Lovely', 'Joyful', 'Wisely', 'SuxVat')
	print('Number of animals person in the world is', len(person))
	new_person= 'Rac Ruoi', 'Cat','Dog' ,person
	print('Number of cages in the world is', len(new_person))
	print('All animals person in new world are', new_person)
	print('Last animal person brought from old world is', new_person[2])
	print('Number of animals person in the new world is',
			len(new_person)-1+len(new_person[2]))
elif(sys.argv[1]=='2'):
	#Dictionary
	tudien={
		'po':'Popo or bobo is meaning idiot',
		'tada':' goodbye ',
		'xinchao':'hello'
		}
	print("po have meaning is ",tudien['po'])
	#Deleting a key-value pair
	del tudien['tada']
	print('\nThere are {} word in the book\n'.format(len(tudien)))
	for tu, nghia in tudien.items():
		print('{} mean {}'.format(tu,nghia))
	tudien['Ngoc'] ='dump'
	if 'Ngoc' in tudien:
		print('Ngoc mean ',tudien['Ngoc'])
elif(sys.argv[1]=='3'):
	print('#Sequence')
	dancuu=['con1','cuu2','andy','suuzy']
	name = 'lucy'
	print('Con so 0 la',dancuu[0])
	print('Con so 1 la',dancuu[1])
	print('Con so 2 la',dancuu[2])
	print('Con so 3 la',dancuu[3])
	print('Con so -1 la', dancuu[-1])
	print('Con so -2 la', dancuu[-2])
	print('Chu dau tien la', name[0])

else:
	print('Sorry, your command is "{}"  not here,go try something else. Bye'
			.format(sys.argv[1]))
