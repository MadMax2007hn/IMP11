import random

global answer
global math_score
global number1
global number2
global correctanswer

def math_quiz():
    answer = 0
    math_score = 0
    correct = 0
    falsch = 0
    durchlauf = input("Durchläufe: ")
    anzahld = 0
    while int(durchlauf) != int(anzahld):
        number1 = random.randint(0, 10)
        number2 = random.randint(0, 10)
        answer = input(str(number1) + " + " + str(number2) + " = ")
        correct = number1 + number2
        if answer == "stop":
            break
        elif answer == "score":
            print("Score: " + str(math_score))
            print("Fehler: " + str(falsch))
        elif int(answer) == int(correct):
            math_score +=1
            anzahld += 1
        else:
            print(str(number1) + " + " + str(number2) + " = " + str(correct))
            falsch += 1
            anzahld += 1
    print("Score: " + str(math_score))
    print("Fehler: " + str(falsch))



math_quiz()
