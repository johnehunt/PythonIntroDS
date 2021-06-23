# Create a generator expression
gen = (x * 2 for x in range(10))

# Use the generator expression
for i in gen:
    print(i, end=', ')

print()
