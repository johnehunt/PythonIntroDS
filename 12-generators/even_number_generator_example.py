# Example of generating a set of even numbers
# The generator itself has a loop

def evens_up_to(limit):
    value = 0
    while value <= limit:
        yield value
        value += 2


for i in evens_up_to(6):
    print(i, end=', ')

print('\n', '-' * 20)

for i in evens_up_to(4):
    print('i:', i)
    print('\t', end='')

    for j in evens_up_to(6):
        print('j:', j, end=', ')

    print('')

# Don't have to use in a loop can explicitly
# request the next value
evens = evens_up_to(4)
print(next(evens), end=', ')
print(next(evens), end=', ')
print(next(evens))
