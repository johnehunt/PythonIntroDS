# Working with Sets

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)  # show that duplicates have been removed
print(len(basket))

# Loop through a set
for item in basket:
    print(item)

# Check to see if a value is contained in a set
print('apple' in basket)

# Remove a 'value' from a set
basket.remove('apple')  # removes value or raises an exception if the value is not present
basket.discard('apricot')  # does not raise an exception if value not present
print(basket)

# Update a set with a value (if not already present)
basket.add('apricot')
print(basket)

# Update a set with multiple values - if values not alreayd present
basket = {'apple', 'orange', 'banana'}
basket.update(['apricot', 'mango', 'grapefruit'])
print(basket)

# Empty all contents from a set
basket.clear()
print(basket)

# Apply set like operators
s1 = {'apple', 'orange', 'banana'}
s2 = {'grapefruit', 'lime', 'banana'}
print('s1', s1)
print('s2', s2)

print('Union:', s1 | s2)
print('Union:', s1.union(s2))

print('Intersection:', s1 & s2)
print('Intersection:', s1.intersection(s2))

print('Difference:', s1 - s2)  # between s1 and what is in s2
print('Difference:', s1.difference(s2))

print('Symmetric Difference:', s1 ^ s2)  # returns all those items only in 1 set
print('Symmetric Difference:', s1.symmetric_difference(s2))

# A tuple in a set
s1 = {(1, 2, 3)}
print(s1)

# Can't put a set intside a set - will generate an exception
# s2 = {{1, 2, 3}}
# print(s2)

# Need to convert sets and lists into frozensets or tuples to nest inside sets
s2 = {frozenset({1, 2, 3})}
print(s2)

s3 = {tuple([1, 2, 3, 2, 1])}
print(s3)
