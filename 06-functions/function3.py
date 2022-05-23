# Examples of functions that return values

def square(n):
    return n * n


# Store result from square in a variable
result = square(4)
print(result)
# Send the result from square immediately to another function
print(square(5))
# Use the result returned form square in a conditional expression
if square(3) < 15:
    print('Still less than 15')


# Function returning multiple values
def swap(a, b):
    return b, a


a = 2
b = 3
x, y = swap(a, b)
print(x, ',', y)
print('----')

z = swap(a, b)
print(z)


# Function with arbitrary Parameter List
def greeter(*args):
    for name in args:
        print('Welcome', name)


greeter('John', 'Denise', 'Phoebe', 'Adam', 'Gryff', 'Natalia')
