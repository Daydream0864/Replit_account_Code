import time
import os

todolist = []
def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')
  
def printslist():
  print()
  for todol in todolist:
    print(todol)
  print()


def edit():
  printslist()
  item = input("What do you want to edit?\n")
  new = input("What do you want to change it to?\n")
  if item in todolist:
   todolist.remove(item)
   print(f"Removed '{item}' from the list.")
   todolist.append(new)
   print(f"Added '{new}' to the second list.")
  elif item not in todolist:
    print("not in there")
  else:
   print(f"'{item}' is not in the list. No changes made.")


while True:
  print("To Do List Manager:")
  print()
  print("dd for my solution for edit\n")
  menu = input("Do you want to view, add, edit, or remove an item from the to do list? ")
  if menu == "view":
    printslist()
  ##############################
  elif menu == "add":
    todo = input("todo text: ")
    if todo not in todolist:
     todolist.append(todo)
    else:
      print(f"{todo},allready there")
  ###########################    
  elif menu == "edit":
    printslist()
    todo = input("What do you want to edit?\n")
    new = input("What do you want to change it to?\n")
    for i in range(0,len(todolist)):
       if todolist[i]==todo:
         todolist[i]=new
  #############
  elif menu == "dd":
    edit()
  ########################
    
  elif menu == "remove":
    printslist()
    removelist = input("What do you want to remove? ")
    if removelist in todolist:
      sure = input("Are you sure you want to remove this? ")
      if sure[0] == "y":
        todolist.remove(removelist)
      else:
        continue
    else:
      print(f"{removelist} not on the list")
      continue

  ########################
  
  elif menu == "del": # easy knew it
    todolist = []
  ##############################  
  time.sleep(1)
  print()
  clear_screen()




# if check[0] == "y":: Here, the code checks if the first character of the user’s input (stored in check) is equal to the letter “y”.
#If the user’s input starts with “y” (indicating “yes”), the condition is met, and the removal process proceeds.

#User Input: edit
#item = input("What do you want to edit?\n").title(): This line prompts the user to input a string (presumably an item from their to-do list). The .title() method is then applied to the input, which capitalizes the first letter of each word in the string (making it title case).
#User Input (Again):
#new = input("What do you want to change it to?\n").title(): Similar to the previous line, this prompts the user to input another string (presumably the updated value they want to set for the item). Again, the .title() method is applied to capitalize the first letter of each word.
#Loop through the To-Do List:
#for i in range(0,len(todolist)):: This loop iterates through the indices of the todolist (which presumably contains the user’s to-do items).
#Check if the Item Exists:
#if todolist[i]==item:: Inside the loop, this condition checks whether the current item in the todolist matches the user-provided item.
#Update the Item:
#todolist[i]=new: If the condition is met (i.e., the current item matches the user’s input), the code updates the item in the todolist by replacing it with the new value (new).






#toDolist = []
#print("To Do List Manager:")





#while True:
  #menu = input("add or remove: ")

  #printslist()
 # if menu == "view":
 #   printslist()
 # if menu == "add":
 #   todo = input("todo text: ")
 #   toDolist.append(todo)
 # elif menu == "remove":
 #   todo = input("todo text:remove ")
  #  if todo in toDolist:
  #    toDolist.remove(todo)
 #   else:
 #     print(f"{todo} not on the list")
 # printslist()
