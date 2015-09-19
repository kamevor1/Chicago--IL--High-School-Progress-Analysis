__author__ = 'kofia_000'
import csv
# this command will open the CVS file
f = open('chicago_High_school_progress_report.csv')
csv_f = csv.reader(f)

for row in csv_f:
  print (row)

# This command will list the name of the schools with the 4-Year and 5-Year graduation rates
import csv

f = open('chicago_High_school_progress_report.csv')
csv_f = csv.reader(f)

for row in csv_f:
  print (row[1], row[2], row[3])
