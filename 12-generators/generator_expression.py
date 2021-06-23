# Create a generator expression
gen = (x * 2 for x in range(10))

for i in gen:
    print(i)
