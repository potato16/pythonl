
import sys
import python103 
print('The command line arguments are:')
for i in sys.argv:
	print(i)
print (python103.total.__doc__)	
print('\n\nThe PYTHONPATH is', sys.path,'\n')
print(python103.say_hello(sys.argv[1],sys.argv[2]))
