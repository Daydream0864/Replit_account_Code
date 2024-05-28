print("Grade Generator")
print("===============")
#################
testname = input("Name of the test ")
maxscore = int(input("max score you can achive "))
userscore = int(input("your score "))

#######################
#50 = 100
#0.5 = 1
#30 = 60
userscore_percentage = userscore / (maxscore/100) 


if round(userscore_percentage, 2) > 90:
  print("A+")
elif userscore_percentage >= 80 and userscore_percentage <= 89:
  print("A")
elif userscore_percentage >= 70 and userscore_percentage <= 79:
  print("B")
elif userscore_percentage >= 60 and userscore_percentage <= 69:
  print("C")
elif userscore_percentage >= 50 and userscore_percentage <= 59:
  print("D")
  print(userscore_percentage)
else:
  print("under 50")


