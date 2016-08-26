"""Follow the chain , pythonchangllenge.com  shitty,
What is chain, where, how, aaaaaa"""
import logging
import urllib.request
logging.basicConfig(filename="chaintracer.log",
		level=logging.DEBUG,
		filemode='w')
print("Creating log file at: ",logging)
i =1
uri='http://www.pythonchallenge.com/pc/def/linkedlist.php'
nothing ='12345'
while True:
#if True:
	print("FUll RETARD",i)
	
	fulluri=uri+"?nothing="+nothing
	nothing=''
	while True:
		try:
			response = urllib.request.urlopen(fulluri)
			break
		except:
			print("Failed. Try again")
	html = response.read().decode()
	logging.debug(html)
	logging.debug(i)
	if 'and the next nothing is' in html:
		for char in html:
			if char.isnumeric():
				nothing +=char
	else:
		print("Master! Help me!!")
		print("He said: ",html)
		nothing=input("Notice me! Next nothing is:")
	#nothing=html[-5:].decode()
	if nothing=='Done':
		print('I'm Done. Oh, thank you master! Enjoy your next challenge. Fighting ^-^')
	i+=1
	print(nothing)

