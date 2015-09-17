import csv
import sys
import operator
#this will open our CVS file
with open("chicago High school progress report.csv","rb") as source:
print("This program is designed to study the progress of Chicago public high schools\n") 
print("To do so, we will analyze some data and make some comparisons\n") 
print("First we will show you the average of 4-Year and 5-Year graduation rate\n") 
first_question = input('''Would you like to find out the average? Type "yes" if you do, and press "Enter" \n\n''') #takes input of yes or no to see whether user wants to find average of numbers
import statistics
print("The 4 Year High School Graduation Rate Percentage in Chicago is :")
print(100*statistics.mean([0.65, 0.50, 0.56, 0.47, 0.82, 0.70, 0.77, 0.84, 0.69, 0.10, 0.18, 0.73, 0.69, 0.74, 0.81, 0.78, 0.65, 0.74, 0.72, 0.69, 0.60, 0.56, 0.83, 0.60, 0.13, 0.62, 0.66, 0.83, 0.51, 0.60, 0.55, 0.56, 0.59, 0.79, 0.73, 0.51, 0.63, 0.71, 0.89, 0.84, 0.91, 0.62, 0.74, 0.70, 0.81, 0.77, 0.72, 0.66, 0.44, 0.52, 0.46, 0.35, 0.53, 0.43, 0.44, 0.50, 0.37, 0.46, 0.62, 0.56, 0.59, 0.86, 0.91, 0.40, 0.31, 0.61, 0.79, 0.84, 0.39, 0.42, 0.62, 0.51, 0.58, 0.49, 0.76, 0.53, 0.40, 0.89, 0.78, 0.69, 0.54, 0.55, 0, 0.05, 0.77, 0.01, 0.98, 0.15, 0.74, 0.74, 0.76, 0.91, 0.69, 0.63, 0.93, 0.41, 0.59, 0.72, 0.04, 0.63, 0.00, 0.76, 0.53, 0.39, 0.81, 0.40, 0.60, 0.70, 0.87, 0.85, 0.78, 0.69, 0.85, 0.54, 0.34, 0.70, 0.73, 0.67, 0.80, 0.57, 0.45, 0.66, 0.19, 0.68, 0.48, 0.81, 0.65]))
print("While The 5 Year High School Graduation Rate Percentage in Chicago is :")
print(100*statistics.mean([0.67, 0.66, 0.70, 0.62, 0.68, 0.74, 0.82, 0.71, 0.20, 0.72, 0.86, 0.74, 0.83, 0.91, 0.84, 0.75, 0.84, 0.75, 0.68, 0.66, 0.70, 0.79, 0.78, 0.06, 0.68, 0.68, 0.80, 0.62, 0.65, 0.57, 0.71, 0.91, 0.84, 0.91, 0.69, 0.76, 0.79, 0.77, 0.79, 0.65, 0.42, 0.53, 0.51, 0.40, 0.67, 0.49, 0.50, 0.50, 0.53, 0.53, 0.78, 0.59, 0.63, 0.86, 0.93, 0.47, 0.41, 0.67, 0.80, 0.86, 0.48, 0.59, 0.70, 0.54, 0.62, 0.53, 0.78, 0.55, 0.39, 0.88, 0.83, 0.75, 0.55, 0.68, 0, 0.80, 0.97, 0.86, 0.76, 0.82, 0.95, 0.79, 0.56, 0.85, 0.53, 0.62, 0.69, 0.43, 0.62, 0.42, 0.80, 0.54, 0.47, 0.82, 0.71, 0.72, 0.75, 0.81, 0.91, 0.90, 0.77, 0.83, 0.66, 0.42, 0.71, 0.80, 0.84, 0.86, 0.74, 0.60, 0.77, 0.82, 0.71]))
