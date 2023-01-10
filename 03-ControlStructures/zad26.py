#26.	The payment card is secured with a four-digit PIN code (0805). Write a program that checks if the PIN code 
# entered in the payment terminal is correct. The user has up to three possibilities for entering a PIN code. 
# In case of three unsuccessful attempts, the card is blocked. Sample result:
#Enter the PIN code: 2398
#Incorrect...
#Enter the PIN code: 0912
#Incorrect...
#Enter the PIN code: 7860
#Incorrect...
#Sorry, your payment card has been blocked.

pin = int("0805")

attemps = 0

while attemps !=3:
    entered = int(input(f"Enter the PIN code: "))
    if entered == pin:
        print("Correct!")
        break
    else:
        print("Incorrect..")
        attemps+=1

    if attemps ==3:
        print("Sorry, your payment card has been blocked.")
