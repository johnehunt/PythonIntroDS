# Read one line of data

file = open('myfile.txt', 'r')
line_of_data = file.readline()
print(line_of_data, end='')
file.close()
