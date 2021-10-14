import csv

print('Starting to read csv file')
with open('sample.csv') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		print(f'{row[0]}, {row[1]}')

print('Done Reading')
