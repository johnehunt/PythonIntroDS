# Illustrates when yield expressions are executed
def gen_numbers2():
    print('Start')
    yield 1
    print('Continue')
    yield 2
    print('Final')
    yield 3
    print('End')


for i in gen_numbers2():
    print('-', end='')
    print(i, end='')
    print('*')

print('-' * 20)