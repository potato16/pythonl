""" http://www.pythonchallenge.com/ 
Find the little guy surrounded by EXACTLY three big bodyguards on each of its sides"""
import os
import platform
import logging
if platform.platform().startswith('Windows'):
	logging_file = os.path.join(os.getenv('HOMEDRIVE'),
			os.getenv('HOMEPATH'),
			'tracer.log')
else:
	logging_file =os.path.join(os.getenv('HOME'),'tracer.log')
print('Logging to',logging_file)
logging.basicConfig(
	level =logging.DEBUG,
	format='%(message)s',
	filename=logging_file,
	filemode='w'
	
)
f = open('bodyguard.txt')
#tracer = {
#	0:'u',
#	1:'u',
#	2:'u',
#	3:'l',
#	4:'u',
#	5:'u',
#	6:'u',
#	7:'l'
#}
process=0
target =''
#oreka=False
tracer=[]
def processcont(char):
	global process 
#	global oreka
	process +=1
	global target
	target += char
	if len(target)==7:
		tracer.append(target)
		#oreka=True
	logging.debug("{}-{}-{}".format(target,process,char))
def processreset():
	global process
	process= 0
	global target
	target= ''
while True:
	line = f.readline()
	if len(line)==0:
		break
#	if oreka:
#		print("O re Ka")
#		break
#	pv = tracer[process]
	for char in line:
		#print(tracer[process])
		if char.islower():
	#		logging.debug(char)
			if process%4==3:
				print('Kaka')
				processcont(char)
			else :
				processreset()
			
		elif char.isupper():
			#logging.debug(char)
			if process%4==3:
				#print("Keke")
				processreset()
			else :
				processcont(char)
f.close()
print("Found it or not: ",tracer)
f = open('tracer.txt','w')
f.write(''.join(tracer))
f.close()
print("Total numbers of little guys: ",len(tracer))

