height = int(input("Type your height in cm\n" ))
feet = height//30
inches = (height%feet)/2.54

print(f'I am {height} cm tall, i.e. {feet} feet and {inches} inches.')