"""This is a test module"""

print('Hello I am the utils module')


def printer(some_object):
    print('printer')
    print(some_object)
    print('done')


class Shape:

    def __init__(self, id):
        self.id = id

    def __repr__(self) -> str:
        return f"Shape(id=${self.id})"

    def __str__(self):
        return 'Shape - ' + self.id


default_shape = Shape('square')


def _special_function():
    print('Special function')
