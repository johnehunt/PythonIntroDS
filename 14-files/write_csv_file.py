import csv

try:
	print('Creating CSV file')
	with open('sample.csv', 'w') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow(['She Loves You', 'Sept 1963'])
		writer.writerow(['I Want to Hold Your Hand', 'Dec 1963'])
		writer.writerow(['Cant Buy Me Love', 'Apr 1964'])
		writer.writerow(['A Hard Days Night', 'July 1964'])
except Exception as exp:
	print(exp)
