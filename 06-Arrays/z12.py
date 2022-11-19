arr = [[2,5,4], [9,0,3]]

print(arr)

print(f"rows: {len(arr)}, cols: {len(arr[0])} ")

print (arr[0][1])

print (arr[1][2])

for i in arr[1]:
    print(i, end= " ")

print ()

for i in arr:
    for x in i:
        print (x, end= " ")



