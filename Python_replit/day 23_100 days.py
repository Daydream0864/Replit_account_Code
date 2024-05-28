print("Replit Login System")

def logIn():
  count = int(0)
  while True:
    Name = input("What is your username?:")
    pasword = input("What is your password?")
    count +=1
    if Name == "david" and pasword == "lol":
      print("Welcome to Replit!")
      break
    else:
      print("Whoops!. Try again!")
      continue
    print(count)
    