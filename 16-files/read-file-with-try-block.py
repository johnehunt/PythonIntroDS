# Illustrates combining exception / error handling
# with file access

print('Start')
try:
    with open('myfile2.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            print(line, end='')
except FileNotFoundError as err:
    print('oops')
    print(err)

print('Done')
