data = [1, 3, 5, 2, 7, 4, 10]

result = sum(data)
print(f'sum of data: {result}')

result = sum(data, 10)
print(f'sum of data (initial value 10): {result}')

result = sum(data, start=10)
print(f'sum of data (start=10): {result}')

