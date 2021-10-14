# Illustrates basic definition of a class in Python

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age


p1 = Person('John', 36)
p2 = Person('Phoebe', 21)

print('id(p1):', id(p1))
print('id(p2):', id(p2))

print(p1)
print(p2)


