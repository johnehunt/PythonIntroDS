# Working with Strings

my_variable = 'Bob'
print(my_variable)
my_variable = "Eloise"
print(my_variable)

# A multi line string
my_variable = """
Hello
  World
"""
print(my_variable)

my_string = 'Hello World'
print(len(my_string))

string_1 = 'Good'
string_2 = " day"
string_3 = string_1 + string_2
print(string_3)

msg = 'Hello Lloyd you are ' + str(21)
print(msg)

# Range of String operations
msg = 'Hello World'
print(msg.replace("Hello", "Goodbye"))

print('Edward Alan Rawlings'.find('Alan'))
print('Edward John Rawlings'.find('Alan'))
print('James' == 'James') # prints True
print('James' != 'John') # prints True

print("msg.startswith('H')", msg.startswith('H'))
print("msg.endswith('d')", msg.endswith('d'))

print('some_string.upper()', msg.upper())

print('sub string: ', 'Hello-World'[1:5])
