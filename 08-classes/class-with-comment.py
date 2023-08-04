# Illustrates a class with a docstring comment

class Person:
	""" An example class to hold a persons name and age"""

	def __init__(self, name, age):
		self.name = name
		self.age = age

	def __repr__(self):
		return self.name + ' is ' + str(self.age)


p1 = Person('John', 36)
p2 = Person('Phoebe', 21)

print(p1)
print(p2)
print(p1.__doc__)
