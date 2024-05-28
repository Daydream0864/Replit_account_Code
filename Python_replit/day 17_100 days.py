#complete
print("game start")
print("-----------")
win1 =0
win2 =0
round =0
while True:
  print("ROUND", round +1)
  player1 = input("player1 > r or s or p : ")
  player2 = input("player2 >r or s or p : ")
  round += 1
  if player1 == "r" and player2 =="s":
    win1 +=1
    print("player1 won")
    print(win1,round)
  elif player1 == "s" and player2 =="p":
    win1 +=1
    print("player1 won")
    print(win1,round)
  elif player1 == "p" and player2 == "r":
    win1 +=1
    print("player1 won")
  ######player one lose
  elif player1 == "r" and player2 == "p":
    win2 +=1
    print("player1 lose")
    print(win2,round)
  elif player1 == "s" and player2 == "r":
    win2 +=1
    print("player1 lose")
  elif player1 == "p" and player2 == "s":
    win2 +=1
    print("player1 lose")
  else:
    print("DRAW")
  ##############
 

  ###########
  if  win1 == 3:
    print("player1",win1, "wins")
    exit()
  elif win2 == 3:
    print("player2",win2, "wins")
    exit()
  else:
    continue
  