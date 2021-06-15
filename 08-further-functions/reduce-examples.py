# Provides an example of using the reduce function

# Note must import reduce from functools module in Python 3
from functools import reduce

data = [1, 3, 5, 2, 7, 4, 10]

# Using a lambda
result = reduce(lambda total, value: total + value, data)
print(f'reduce using lambda: {result}')


# Using a named function
def generate_total(running_total, value):
    return running_total + value


result = reduce(generate_total, data)
print(f'reduce using named function: {result}')

result = reduce(generate_total, data, 10)
print(f'reduce using named function (start 10): {result}')


# Simpler version is to use sum
result = sum(data)
print(f'sum of data: {result}')

result = sum(data, 10)
print(f'sum of data (start 10): {result}')
