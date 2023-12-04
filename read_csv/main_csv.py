import csv

with open('read_csv/doc.csv', mode = 'r') as file :
    csv_reader = csv.DictReader(file) 
    for line in csv_reader :
        print(line)