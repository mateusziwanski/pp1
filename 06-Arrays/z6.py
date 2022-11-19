t = [2,3,7,5,4]

print (t)
print (len(t))
print (t[0])
print (t[1])
print (t[-1])
print (t[-2])
print (t[0]+ t[-1])
print (t[len(t)//2])
for i in t:
    print (i, end = " ")
print()
for i in t[0: (len(t)//2)+1]:
    print(i, end = " ")