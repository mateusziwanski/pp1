# 24.	Write a program that creates the following pattern. Sample result:
#* 
#* * 
#* * * 
#* * * * 
#* * * * * 
#* * * * 
#* * * 
#* * 
#*

for i in range (1,6):
    for j in range (i):
        print ("*", end= "")
    print("")

for i in range (4,0,-1):
    for j in range (i):
        print ("*", end="")
    print("")
