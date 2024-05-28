import random
import os
import time


def attack():
  num1 = int(charstrengh1)
  num2 = int(charstrengh2)
  if num1 > num2:
    diff = num1 - num2
  elif num1 == num2:
    diff = int(5)
  else:
    diff = num2 - num1
  print("The difference of", num1, "and", num2, "is", diff)
  return diff


#((rollDice(6)*rollDice(12))/2)+10 for simpler math couldnt get it working
def dicehealth():
  random6 = random.randint(1, 6)
  random12 = random.randint(1, 12)
  roll = (random6 * random12) / int(2)
  endroll = roll + int(10)
  return str(round(endroll))


def dicestrength():
  random6 = random.randint(1, 6)
  random12 = random.randint(1, 12)
  roll = (random6 * random12) / int(2)
  endroll = roll + int(12)
  return str(round(endroll))


while True:
  print("Character Builder")
  char1 = input("Name your legend ")
  type1 = input("Character Type (human, imp, wizard, elf, etc.) ")
  time.sleep(1)
  #character(char, type)
  print()
  time.sleep(1)
  print(char1)
  charhealth1 = dicehealth()
  charstrengh1 = dicestrength()
  print("HEALTH: " + charhealth1)
  print("STRENGHT: " + charstrengh1)
  print()

  print("Who are they battling?")

  char2 = input("Name your legend ")
  type2 = input("Character Type (human, imp, wizard, elf, etc.) ")
  print()
  charhealth2 = dicehealth()
  charstrengh2 = dicestrength()
  countr = int(0)

  print(char2)
  print("HEALTH: " + charhealth2)
  print("STRENGHT: " + charstrengh2)
  print()
  os.system("clear")
#####################################
  while int(charhealth2) > int(0) or int(charhealth1) > int(0):
    countr += 1
    print("⚔️ BATTLE TIME ⚔️")
    print("The battle begins!")
    time.sleep(1)
    random1 = random.randint(1, 6)  # player 1
    random2 = random.randint(1, 6)  # player 2
    print(charhealth1, "player1")
    print(charhealth2, "player2")
    print()
    if random1 > random2:
      print(char1, "wins")
      charhealth2 = int(charhealth2) - attack()
      # charhealth2-= attack()
      if int(charhealth2) <= int(0) or int(charhealth1) <= int(0):
        print("ok", countr, "ROUNDS")
        break
    elif random1 < random2:
      print(char2, "wins")
      charhealth1 = int(charhealth1) - attack()
      if int(charhealth2) <= int(0) or int(charhealth1) <= int(0):
        print("ok", countr, "ROUNDS")
        break
    else:
      print(random1, random2, "equal, no attack")
    time.sleep(4)
    os.system("clear")

  time.sleep(1)
  print(charhealth1, "player 1")
  print(charhealth2, "player 2")
  again = input("AGAIN")
  if again == "yes":
    os.system("clear")
    continue
  else:
    os.system("clear")
    exit()
