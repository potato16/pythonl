i = 5
print(i)
i=i+1
print(i)
s='''This is a multi-line string.
This is the second line.'''
print(s)
a=3**4
print(a)
number = 16
tiep = 1
while tiep==1:
	guess = int(input('Enter an number : '))
	if guess== number:
		print('Good, you guessed it.')
		print('(but you do not win any prizes!)')
	elif guess<number:
		print ('No, it id a little higher than that')
	else:
		print('No, it is a little lower than that')
	#print('Done')
	tiep = int(input('Wanna play again: '))
	print (tiep)
print('Done')
