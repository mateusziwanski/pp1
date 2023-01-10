# 11.	Create a program that displays the name of month for a given month number (1 to 12). 
# Define a month(n) function that returns the name of month for the number n. Store month names in an array. 
# Using defined function, display month names for the following month numbers: 1, 2, 11, 12.

def month(mon):
    months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
    mon = months[mon-1]
    return mon

print (month(1))
print (month(2))
print (month(11))
print (month(12))