def greeter(name, message='Live Long and Prosper'):
    print('Welcome', name, '-', message)


greeter('Eloise')
greeter('Eloise', 'Hope you like Rugby')


def greeter(name, title='Dr', prompt='Welcome', message='Live Long and Prosper'):
    print(prompt, title, name, '-', message)


greeter(message='We like Python', name='Lloyd')
greeter('Lloyd', message='We like Python')
