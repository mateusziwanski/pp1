add = input("Podaj nazwę produktu: ")
with open ("shopping.txt", 'a') as f:
    f.write(add + "\n")