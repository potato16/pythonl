def reverse(text):
	#wow this can reverse a string
	#how can i make "rise to vote , sir." is palindrome
	return text[::-1]
def cleartext(text):
	rtext =''
	for c in text:
		if c.isalpha():
			rtext+=c.lower()
	return rtext
def is_palindrome(text):
	textcleared =cleartext(text)
	print (textcleared)
	return textcleared == reverse(textcleared)
something = input("Enter text: ")
if is_palindrome(something):
	print('Yes, it is palindrome')
else:
	print('No, it is not a palindrome')

