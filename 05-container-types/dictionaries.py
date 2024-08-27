# Set up a dictionary
cities = {'Wales': 'Cardiff',
          'England': 'London',
          'Scotland': 'Edinburgh',
          'Northern Ireland': 'Belfast',
          'Ireland': 'Dublin'}

print(len(cities))
print(cities)

# Retrieve values for keys
print('cities[Wales]:', cities['Wales'])  # returns value for key or throws an exception
print('cities.get(Ireland):', cities.get('Ireland'))  # Returns value for key - does nto throw an exception if not present

print(cities.values())
print(cities.keys())
print(cities.items())

print('Wales' in cities)
print('France' not in cities)

for country in cities:
    print(country, end=', ')
    print(cities[country])

# Add an entry to a dictionary
cities['Wales'] = 'Swansea'
print(cities)

# Empty the dictionary of all values
cities.clear()
print(cities)

cities = {'Wales': 'Cardiff',
          'England': 'London',
          'Scotland': 'Edinburgh',
          'Northern Ireland': 'Belfast',
          'Ireland': 'Dublin'}
print(cities)

# Remove key from dictionary and return value
cities.pop('Northern Ireland')
print(cities)

# Remove key from dictionary
del cities['Scotland']
print(cities)

print('-' * 25)

d = {'one': 1, 'two': 2}
print(d)
print(type(d))
print(d['two'])
d['three'] = 3
print(d)
del d['two']
print(d)

# Values can be containers
seasons = {'Spring': ('Mar', 'Apr', 'May'),
           'Summer': ('June', 'July', 'August'),
           'Autumn': ('September', 'October', 'November'),
           'Winter': ('December', 'January', 'February')}
print(seasons['Spring'])
print(seasons['Spring'][1])

print('-' * 25)

print(d.keys())
print(d.values())

for e in d.values():
    print(e)

print(d.items())

d['four'] = 4
print(d.keys())
print(sorted(d.keys()))

key = 'England'

if key in cities:
    print('Key is present, value = ', cities[key])
else:
    print('Key not present')

