__author__ = 'kofia_000'
import csv

f = open('chicago_High_school_progress_report.csv')
csv_f = csv.reader(f)

for row in csv_f:
  print (row)