import time
import os
#My biggest mistake was put the 'else' statment. Now, when a letter doesn’t match any of the conditions, the else clause will execute, resetting the color to the default.  the color are switching and are active. if a diffent statement comes it will switch. it works booth with my function and color command.

def colorchange(color):
  if color == "red":
    print('\033[31m', end='')
  elif color == "white":
    print('\033[0m', end='')
  elif color == "blue":
    print('\033[96m', end='')
  elif color == "yellow":
    print('\033[33m', end='')
  elif color == "green":
    print('\033[32m', end='')
  elif color == "purple":
    print('\033[35m', end='')
print("What sentence do you want rainbow-insing?")
string = "Become one with the rainbow my young rainbowan".lower()
print(string)
for letter in string:
  if letter == "r":
    #colorchange("red")
    print("\033[31m", end="")
  elif letter == str("b"):
    #colorchange("blue")
    print("\033[34m", end="")
  elif letter == " ":
    #colorchange("white")
    print("\033[0m", end="")
  elif letter == "y" :
    #colorchange("yellow")
    print("\033[33m", end="")
  elif letter == "g":
    print("\033[32m", end="")   
    #colorchange("green")
  #else:
    #print('\033[0m', end='')
  print(letter, end="")

