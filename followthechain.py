"""Follow the chain , pythonchangllenge.com  shitty,
What is chain, where, how, aaaaaa"""
import urllib.request
i =1
uri='http://www.pythonchallenge.com/pc/def/linkedlist.php'
nothing ='12345'
while i<=400:
#if True:
	print("FUll RETARD")
	fulluri=uri+"?nothing="+nothing
	response = urllib.request.urlopen(fulluri)
	html = response.read()
	nothing=html[-5:].decode()
	
	i+=1
	print(nothing)

