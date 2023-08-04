# Definition of a class with some basic behaviour

class Person:
	""" An example class to hold a persons name and age"""

	def __init__(self, name, age):
		self.name = name
		self.age = age

	def __repr__(self):
		return self.name + ' is ' + str(self.age)

	def birthday(self):
		print ('Happy birthday you were', self.age)
		self.age += 1
		print('You are now', self.age)


p3 = Person('Adam', 21)
print(p3)
p3.birthday()
print(p3)
