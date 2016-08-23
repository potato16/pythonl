''' convert string by change these string ascii code character to 2'''
strencode = input('Enter code text here: ')
strdecode=''
for char in strencode:
	c=char
	if  char.isalpha():
		c = chr((ord(char)+2-97)%26+97)
	strdecode +=c
print('String decode to: ',strdecode)
