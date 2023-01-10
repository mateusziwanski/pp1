# 9.	An array contains a list of Polish names: Genowefa, Onufry, Celestyna, Alojzy, Pankracy. 
# Create a program that displays the longest name (consisting of the largest number of characters). Sample result:
# Names: Genowefa Onufry Celestyna Alojzy Pankracy
# Longest name: Celestyna

names = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]

longest = names[0]

for i in names:
    if len(i) > len(longest):
        longest = i 
for i in names:
    print(i, end = " ")
print (f"\nLongest name: {longest}") 