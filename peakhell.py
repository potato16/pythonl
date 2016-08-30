import pickle
#import urllib.request
#source = urllib\
#.request\
#.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")\
#.read()\
#.decode()
peakfile = 'banner.p'
f = open(peakfile,'rb')
okfile = pickle.load(f)
tong =0
for item in okfile:
	print(item)
#	print(''.join(elmt[0]*elmt[1]  for elmt in item))
#	for sub in item:
#		print(sub)	
#		if sub[0]=='#':
#			tong = tong + int(sub[1])
#print (tong)
print('what the fuck')
#print(source)
