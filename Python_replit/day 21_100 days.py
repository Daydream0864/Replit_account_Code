print("Math Game!")

multi = int(input("Name your multiples: "))
counter = 0
for i in range(1, 11,):
  answer = int(input("guess"))
  correct_answer = i*multi
  if answer ==  correct_answer:
    print("You got it right!")
    counter += 1
  else:
    print("That's not correct. It should have been", correct_answer)
if counter == 10:
  print("Wow! A perfect score! 🥳")
else:
  print("You got", counter, "out of 10 correct.")