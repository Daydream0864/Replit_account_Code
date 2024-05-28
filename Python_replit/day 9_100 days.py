print("Generation Generator")
print("--------------------")
###########################
age = int(input("What generation are you a part of?, what year were you born?"))

if age > 1925 and age < 1946:
  print("Traditionalists")
elif age > 1947 and age < 1964:
  print("Baby Boomers")
elif age > 1965 and age < 1981:
  print("Generation X")
elif age > 1982 and age < 1995:
  print("Millenials")
else:
  print("gen z or not valid")

