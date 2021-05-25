def get_integer_input(message):
    """
    This function will display the message to the user
    and request that they input an integer.

    If the user enters something that is not a number
    then the input will be rejected
    and an error message will be displayed.

    The user will then be asked to try again."""

    value_as_string = input(message)
    while not value_as_string.isnumeric():
        print('The input must be an integer')
        value_as_string = input(message)

    return int(value_as_string)


age = get_integer_input('Please input your age: ')
print('age is', age)

print(get_integer_input.__doc__)