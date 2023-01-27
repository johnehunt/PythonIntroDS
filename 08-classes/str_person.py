# A class that can be converted to a string
# for example for printing and logging purposes

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def __str__(self):
		return self.name + ' is ' + str(self.age)

	def __repr__(self):
		return f'Person(name={self.name}, age={self.age})'


p1 = Person('John', 36)
p2 = Person('Phoebe', 21)

print(p1)
print(p2)

print('-' * 25)

px = p1

print(p1)
print(px)

print('id(p1):', id(p1))
print('id(px):', id(px))

data = [p1, p2]
print(data)

