height = int(input("Enter your height in cm\n" ))
weight = int(input("Enter your weight in kg\n" ))

BMI = (weight/(height/100)**2)
print(f'Your BMI is {BMI}')