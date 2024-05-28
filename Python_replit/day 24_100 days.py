import random
def dice(side):
  while True:
    again = input("Roll again?")
    if again == "yes":
      print(random.randint(1,side))
    else:
      break

dicesides = int(input("How many sides?:"))
dice(dicesides)