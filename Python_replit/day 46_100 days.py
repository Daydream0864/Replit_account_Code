clue = {}
def prettyPrint():
  print()

  for key, value in clue.items():
    # moves along every 'key:subDictionary' pair and outputs the key (the name of the character).
    print(key, end=": ")
    for subKey, subValue in value.items():
      # (nested) `for` loop moves along every subkey and subvalue in each subDictionary.
      print(subKey, subValue, end=" | ")
    print()

while True:
  name = input("Name: ")
  element = input("element: ")
  weapon = input("Weapon: ")

  clue[name] = {"location": element, "weapon":weapon} 
  print("----------")
  print()
  prettyPrint()
  q = input("more ").lower()
  
  if q == "y":
    continue
  else:
    break