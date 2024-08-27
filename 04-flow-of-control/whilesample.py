# Illustrates basic while loop

valid_data = False

while not valid_data:
    age = int(input('Please enter your age: '))
    if age < 0 or age > 120:
        print('invalid Age')
    else:
        valid_data = True

print()  # not part of the while loop

print('Done')
