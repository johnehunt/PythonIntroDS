# Examples of checking for membership of a container

# Tuples
fruit = ('apple', 'pear', 'orange', 'plum', 'apple')
if 'orange' in fruit:
    print('orange is in the Tuple')

if 'orange' not in fruit:
    print('orange is NOT in the Tuple')

# Lists
list1 = ['John', 'Paul', 'George', 'Ringo']
if 'Pete' in list1:
    print('Pete in the list')
else:
    print('Pete not in the list')

# Dictionaries
cities = {'Wales': 'Cardiff',
          'England': 'London',
          'Scotland': 'Edinburgh',
          'Northern Ireland': 'Belfast',
          'Ireland': 'Dublin'}
if 'Wales' in cities:
    print('We know the capital of Wales')