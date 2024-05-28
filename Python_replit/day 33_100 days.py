import time

toDolist = []
print("To Do List Manager:")


def printslist():
  print()
  for todol in toDolist:
    print(todol)
  print()


while True:
  menu = input("add or remove: ")

  printslist()
  if menu == "view":
    printslist()
  if menu == "add":
    todo = input("todo text: ")
    toDolist.append(todo)
  elif menu == "remove":
    todo = input("todo text:remove ")
    if todo in toDolist:
      toDolist.remove(todo)
    else:
      print(f"{todo} not on the list")
  printslist()
