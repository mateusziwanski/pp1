# 18.	There are coins of 1, 2 and 5 Polish Zlotys (PLN). Write a program showing any amount (natural number) 
# read from the keyboard with as few coins as possible.
#Enter the amount in PLN: 18
#The amount of PLN 18 in coins:
#5 zł – 3 
#2 zł – 1 
#1 zł – 1


amount = int(input("Enter the amount in PLN: "))


sum = 0

#sprawdzenie 5 zł 
coin = 5
if amount >= coin:
    x5 = int(amount/coin)
    print(f"5 zł - {x5}")
    amount = amount- x5*coin
else: 
    print ("5 zł - 0")

#sprawdzenie 2 zł

coin = 2
if amount >= coin:
    x2 = int(amount/coin)
    print(f"2 zł - {x2}")
    amount = amount- x2*coin
else: 
    print ("2 zł - 0")

#sprawdzenie 1 zł

coin = 1 
if amount == coin:
    print ("1 zł - 1")
else:
    print ("1 zł - 0")


