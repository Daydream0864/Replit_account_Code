print("Welcome to Guess the Number.")
print()
print("Guess a number between 1 and 1,000,000 and I will tell you if you are too low, too high, or get it correct.")
print()
print("Let's play!")

numbercorrect = 1337

count = 0
while True:
  numinput = int(input("what is you guess? "))
  count += 1
  if numinput < numbercorrect:
    print("to low")
  elif numinput > numbercorrect:
    print("to high")
  elif numinput == numbercorrect:
    print(numbercorrect,"took you", count,"times", "you guessed it")
    break
  else:
    
    exit()
print("That is not a number I recognize.")
# numbercorrect =1337 and never be zero(0) infanite loop accidently
#while numbercorrect != int(0):
#  num = int(input("what is you guess?"))
#  count += 1
#  if num < numbercorrect:
#    print("to low")
#  elif num > numbercorrect:
#    print("to high")
#  elif num == numbercorrect:
#    print(numbercorrect,"took you", count,"times", "you guessed it")
#    break
  
 # else:
 #   print("That is not a number I recognize.")
 #   exit()
