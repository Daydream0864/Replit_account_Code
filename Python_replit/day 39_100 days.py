import random
import os
import time

listOfWords = [
  "british", "suave", "integrity", "accent", "evil", "genius", "Downton"
]

wordChosen = random.choice(listOfWords)
hangmanlist = list(wordChosen)

def hide_word(word):
  return "_" * len(word)
    
#def remove_at(index, input_string):
  #return input_string[:index] + input_string[index + 1:]
def print_secret_word(secret_word, guessed_letters):
  for letter in secret_word:
      if letter in guessed_letters:
          print(" {} ".format(letter), end="")
      else:
          print(" _ ", end="")
  print("\n")
while True:
  count = 0
  hidden_word = hide_word(hangmanlist)
  inputletter = input("Choose a letter:")
  underscore = hide_word(hangmanlist)

  
  print_secret_word(hangmanlist, inputletter)
  
  print(hangmanlist)

#jedes wort einer nummer zuteilen und diese ersetezen
##############



listOfWords = ["apple", "orange", "grapes", "pear"]
letterPicked = []
lives = 6

word = random.choice(listOfWords)

while True:
  time.sleep(1)
  os.system("clear")
  letter = input("Choose a letter: ").lower()

  if letter in letterPicked:
    print("You've tried that before")
    continue

  letterPicked.append(letter)

  if letter in word:
    print("You found a letter")
  else:
    print("Nope, not in there")
    lives -= 1

  allLetters = True
  print()
  for i in word:
    if i in letterPicked:
      print(i, end="")
    else:
      print("_", end="")
      allLetters = False
  print()

  if allLetters:
    print(f"You won with {lives} left!")
    break

  if lives<=0:
    print(f"You ran out of lives! The answer was {word}")
    break
  else:
    print(f"Only {lives} left")

#####################


   


