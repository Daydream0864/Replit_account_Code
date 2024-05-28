while exit != "yes":
  animalname = input("What animal do you want?: ")
  
  if animalname == "cow":
    print("A cow goes moo.")
  elif animalname == "cat":
    print("meow")
  elif animalname == "lemur":
    print("Ummm...the Lesser Spotter Lemur goes awooga.")
  else: 
    print("I don't know that animal sound. Try again.")
  
  exit = input("Do you want to exit?:")
print("EXIT")