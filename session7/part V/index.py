from random import randint, choice
count = 0
while True:
    number1 = randint(1, 100)
    number2 = randint(1, 100)

    #print(number1, number2)

    operation = ["+", "-"]

    randomOper = choice(operation)

    step = randint(-1,1)

    if randomOper == "+": 
        result = number1 + number2
    elif randomOper == "-":
        result = number1 - number2
    errResult = result + step
    print(number1, randomOper, number2, "=", errResult)
    user = input("True or False? ")

    if step == 0: 
        errResult = result
        if user == "T" or user == "t":
            print("You won")
            count = count + 1
            print(count)

        elif user == "F"or user == "f":
            print ("hung phan")
            print(count)
            break
        else:
            break
    else:
        errResult = result + step
        if user == "T" or user == "t":
            print ("hung phan")
            print(count)
            break
        elif user == "F" or user == 'f':
            print("You won")
            count = count + 1
            print(count)
        else:
            break
