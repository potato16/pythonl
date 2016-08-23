''' Find the little guy surrounded by EXACTLY three big bodyguards on each of its sides'''
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
tracer = {
	0:True,
	1:True,
	2:True,
	3:False,
	4:True,
	5:True,
	6:True,
	7:False
}
process=0
target =''
def processcont(char):
	global process 
	process +=1
	global target
	target += char
#	logging.debug("{}-{}-{}".format(target,process,char))
def processreset():
	global process
	process= 0
	global target
	target= ''
while True:
	line = f.readline()
	if len(line)==0:
		break
	if process==8:
		break
#	pv = tracer[process]
	for char in line:
		#print(tracer[process])
		if char.islower():
	#		logging.debug(char)
			if tracer[process]:
				print('Kaka')
				processcont(char)
			else :
				processreset()
			
		elif char.isupper():
			logging.debug(char)
			if tracer[process]:
				print("Keke")
				processcont(char)
			else :
				processreset()
f.close()
print("Found it or not: ",target)	

