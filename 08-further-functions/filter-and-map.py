data = [1, 3, 5, 2, 7, 4, 10]
print('data:', data)


def is_even(i):
	return i % 2 == 0


# Filter for even numbers and use map to add 10
new_data = list(map(lambda i: i + 10, filter(is_even, data)))
print('new_data:', new_data)
