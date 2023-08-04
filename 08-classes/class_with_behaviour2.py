# Definition of a class with some additional behaviour

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

	def calculate_pay(self, hours_worked):
		rate_of_pay = 7.50
		if self.age >= 21:
			rate_of_pay += 2.50
		return hours_worked * rate_of_pay

	def is_teenager(self):
		return self.age < 20


p2 = Person('Phoebe', 21)
p3 = Person('Adam', 21)
print(p3)
p3.birthday()
print(p3)

pay = p2.calculate_pay(40)
print(f'Pay {p2.name} {pay}')
pay = p3.calculate_pay(40)
print(f'Pay {p3.name} {pay}')
print(f'p2.is_teenager {p2.is_teenager()}')

p1 = Person('John', 36)
print(p1)
del p1
