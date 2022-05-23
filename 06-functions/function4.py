# Arbitrary Parameter Lists


def greeter(*names):
    for name in names:
        print('Welcome', name)


greeter('John', 'Denise', 'Phoebe', 'Adam', 'Gryff', 'Natalia')
