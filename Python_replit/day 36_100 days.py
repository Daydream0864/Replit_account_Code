list = []
def printList():
 print()
 for i in list:
   print(i)
 print()
while True:
  firstname = input("firstname").strip().capitalize()
  lastname  = input("lastname").strip().capitalize()
  newname = str(f"{firstname} {lastname}")
  
  if newname not in list:
    list.append(newname)
  else:
    print("ERROR: Duplicate name")
  printList()