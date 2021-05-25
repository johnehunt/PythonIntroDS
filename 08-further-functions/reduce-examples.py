# Provides an example of using the reduce function

# Note must import reduce from functools module in Python 3
from functools import reduce

data = [1, 3, 5, 2, 7, 4, 10]
result = reduce(lambda total, value: total + value, data)
print(f'reduce using lambda: {result}')


def generate_total(running_total, value):
    return running_total + value


result = reduce(generate_total, data)
print(f'reduce using named function: {result}')
