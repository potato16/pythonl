class Person:
	def __init__(self, name):
		self.name = name+' the greatness'
	def say_hi(self):
		print("Hello, my name is ",self.name)
p = Person('Han Thao')
p.say_hi()
