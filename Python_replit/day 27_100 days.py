import random
import os
import time

def character(lol,kik):
  print("Name Your Legend:")
  print(lol)
  print("Character Type (Human, Elf, Wiard, Orc):")
  print(kik)

#((rollDice(6)*rollDice(12))/2)+10 for simpler math couldnt get it working
def dicehealth():
  random6 = random.randint(1,6)
  random12 = random.randint(1,12)
  roll = (random6 * random12)/int(2)
  endroll = roll + int(10)
  return str(round(endroll))
def dicestrength():
  random6 = random.randint(1,6)
  random12 = random.randint(1,12)
  roll = (random6 * random12)/int(2)
  endroll = roll + int(12)
  return str(round(endroll)) 

while True:
  print("Character Builder")
  char = input("Name your legend ")
  type = input("Character Type (human, imp, wizard, elf, etc.) ")
  os.system("clear")
  time.sleep(1)
  character(char, type)
  print()
  time.sleep(1)
  
  print("HEALTH: "+dicehealth())
  print("STRENGHT: "+dicestrength())
  print()
  print("May your name go down in Legend...")
  time.sleep(1)
  again = input("AGAIN")
  if again == "yes":
    os.system("clear")
    continue
  else:
    os.system("clear")
    exit()
