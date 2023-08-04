# Contains example sof handling
# errors and exceptions as well as
# creating / raising your own

def run_calculation(x):
    x / 0


def print_value(i, data_list):
    print(data_list[i])


def print_alt_value(i, data_list):
    if i > len(data_list):
        raise ValueError('Invalid length ' + str(i))
    print(data_list[i])


def my_function(x, y):
    print('my_function in')
    result = x / y
    print('my_function out')
    return result


def f2():
    print('f2 in')
    function_bang()
    print('f2 out')


def function_bang():
    print('function_bang in')
    raise ValueError('Bang!')
    print('function_bang out')


class InvalidAgeException(Exception):
    """ Valid Ages must be between 0 and 120 """

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return 'InvalidAgeException(' + str(self.value) + ')'


class DivideByYWhenZeroException(Exception):
    """ Sample Exception class"""


def divide(x, y):
    try:
        result = x / y
        print(result)
    except Exception as e:
        raise DivideByYWhenZeroException from e


class Person:
    """ An example class to hold a persons name and age"""

    def __init__(self, name, age):
        self.name = name
        self._age = age

    def __str__(self):
        return self.name + ' is ' + str(self._age)

    def set_age(self, value):
        print('In set_age method(', value, ')')
        if isinstance(value, int) & (value > 0 & value < 120):
            self._age = value
        else:
            raise InvalidAgeException(value)


def main():
    # divide(6, 0)

    print('Starting')
    try:
        print('Before my_function')
        my_function(6, 2)
        print('After my_function')
    except ZeroDivisionError as exp:
        print('oops')
    else:
        print('All OK')

    print('Done')

    try:
        my_function(6, 0)
    except ZeroDivisionError as e:
        print(e)
    else:
        print('Everything worked OK')
    finally:
        print('Always runs')

    values = [1, 2, 3, 4]
    try:
        print_alt_value(7, values)
    except Exception as e:
        print(e)

    values = [1, 2, 3, 4]
    try:
        print_value(2, values)
        print_value(3, values)
    except IndexError as e:
        print('Exception: ', e)
    else:
        print('All OK')
    finally:
        print('Always runs')

    try:
        print(divide(3, 0))
    except Exception as e:
        print(e)

    try:
        p1 = Person("Natalia", 22)
        p1.set_age(-1)
    except InvalidAgeException as exp:
        print(f'Exception: {exp}')

    try:
        function_bang()
    except ValueError as ve:
        print(ve)
        raise


if __name__ == "__main__":
    main()
