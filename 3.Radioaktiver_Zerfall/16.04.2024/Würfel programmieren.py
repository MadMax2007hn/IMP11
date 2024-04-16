import random

randNr = random.random()
print(randNr)

if randNr <= 1/6:
    print("1")
elif 1/6 < randNr <= 2/6:
    print("2")
elif 2/6 < randNr <= 3/6:
    print("3")
elif 3/6 < randNr <= 4/6:
    print("4")
elif 4/6 < randNr <= 5/6:
    print("5")
elif 5/6 < randNr <= 1:
    print("6")
else:
    print("Benutzer hat Fehler gemacht")
