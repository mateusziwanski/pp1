#19.	Write a program that calculates a dog's age in dog’s years. For the first two years, a dog's life is equal to 10.5 human years. 
# After that, each dog year is equal to 4 human years. Sample result:
#Enter the dog's age in human years: 15
#The dog's age in dog’s years is 73 years.

def dogs_age(age):
    if age == 1:
        print(f"The dog's age in dog's years is 10.5 years old")
    elif age == 2:
        print(f"The dog's age in dog's years is {int(2*10.5)} years old")
    elif age > 2:
        print(f"The dog's age in dog's years is {int(10.5*2 + 4*(age - 2))} years old")


dogs_age(15)
