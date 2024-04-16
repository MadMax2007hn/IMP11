import random

p = 0.1
counter = 0
while True:
    if random.random() <= p:
        print("Zerfallen, ich habe " + str(counter) + " Jahre überlebt.")
        break
    else:
        print("Lebt weiter")
        counter += 1
