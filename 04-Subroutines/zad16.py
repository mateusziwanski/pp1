# 16.	Each month of a calendar year can be expressed by its name or by a number that indicates the position of the month in year. 
# Define a function month(n) that returns a month name based on the month number (values from 1 to 12). 
# Then create a program and display the name of the month 7.

def month(n):
    months = ["january", "feb", "mar", "apr", "may", "june", "july", "august", "sep", "oct", "nov", "dec"]
    return months[n-1]

print(month(7))
