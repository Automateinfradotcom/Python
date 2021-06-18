import csv

with open('devops.csv' , 'r') as csv_row:
	## Parse the line as comma-delimited
	csv_data = csv.reader(csv_row,  delimiter=',')
print(csv_data)
