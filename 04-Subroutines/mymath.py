# 15.	In the module mymath.py, create the following function definitions:
# a.	read_number() that reads from the keyboard and returns integer number
# b.	generate_number() that creates and returns random integer number in the range of <1,9>

import random

def read_number():

    return int(input("Type int: "))

def generate_number():

    return random.randint(1, 10)