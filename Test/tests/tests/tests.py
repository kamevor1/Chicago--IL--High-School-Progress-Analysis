
import csv

f = open('chicago_High_school_progress_report.csv')
csv_f = csv.reader(f)
#This will print all the schools names with the graduation rates
for row in csv_f:
  print (row)

#This command will print the schools names with the 4-Year graduation rate and 5-Year graduation rate
f = open('chicago_High_school_progress_report.csv')
csv_f = csv.reader(f)

for row in csv_f:
  print (row[1], row[2],row[3])


