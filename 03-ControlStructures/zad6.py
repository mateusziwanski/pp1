limit = 130
speed = int(input("Podaj prędkość\n"))

if speed > limit:
    print("Przekroczona dozwolona prędkość")
if speed <= limit:
    print("Prędkość dozwolona")