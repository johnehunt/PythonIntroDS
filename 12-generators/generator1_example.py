# Basic generator function
def gen_numbers():
    yield 1
    yield 2
    yield 3


for i in gen_numbers():
    print(i)

print('-' * 20)