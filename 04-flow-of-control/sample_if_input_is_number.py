# Illustrates a simple if statement
# Note checks to see if the string that has been input only contains number characters
input_string = input('Please input a number: ')

if input_string.isnumeric():
    print('The number is accepted')
else:
    print('The input is invalid')
