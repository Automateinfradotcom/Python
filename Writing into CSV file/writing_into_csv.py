import csv

with open('devops.csv','a', newline='') as csv_file:
    write_csv = csv.writer(csv_file,  delimiter=',')
    write_csv.writerow(['08-08-2021','68','8888', 'site.com/blog8'])
