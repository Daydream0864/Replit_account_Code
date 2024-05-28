import random
print("Welcome to guess the number")
print()
print("Guess a number between 1 and 100000 ab I will tell you if you are to low or high or get it correct")
print()

numbercorrect = random.randint(1,1000)

count = 0
while True:
    numinput  = int(input("what is your guess"))
    count += 1
    if numinput>numbercorrect:
        print("to low")
    elif numinput < numbercorrect:
        print("top high")
    elif numinput == numbercorrect:
        print("correct")
        break
    else:
        exit()