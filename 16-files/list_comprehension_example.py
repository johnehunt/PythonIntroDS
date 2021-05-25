# Can also use a list comprehension to
# set up a list with the contents of a file

file = open('myfile.txt', 'r')

lines = [line.upper() for line in file]

file.close()
print(lines)
