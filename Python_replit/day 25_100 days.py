import random

print("⚔️ Character Stats Generator ⚔️")

#def dice(dicesize):
 # diceroll = int(input("any size dice"))
  #return diceroll
####no function, no benefit


def sixeightdice():
  rollsix = random.randint(1,6)
  rolleight = random.randint(1,8)
  sum = rolleight * rollsix
  return str(sum) 
  
while True:
  character = input("Name your warrior: ")
  charhealth = sixeightdice()
  print("Their health is:"+ charhealth + "HP")
  more = input("yes or no")
  if more == "yes":
    continue
  else:
    exit()