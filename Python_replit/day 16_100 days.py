#while True:
  #print("This program is running")
  #goAgain = input("Go again?: ")
  #if goAgain == "no":
 #   break
#print("Aww, I was having a good time 😭")
#############
print("Welcome to Name the Song Lyric")
print()
print("Figure out the missing word as quickly as you can!")
print()
count = 0


while True:
  count += 1
  placeholder = input("Never going to ______ you up. ")
  if placeholder == "give":
    print("Well done! It only took you {} attempts.".format(count))
    break
  else:
    print("Nope, try again.")
print("You got the correct lyrics in", count, "attempt(s).")