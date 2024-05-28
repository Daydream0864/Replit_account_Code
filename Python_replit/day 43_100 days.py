import random
def num():
  randomn = random.randint(0, 90)
  return randomn

def printt():
  print(f"{list2d[0][0]} | {list2d[1][0]} | {list2d[2][1]} ")
  print(f"{list2d[0][1]} | {list2d[1][1]} | {list2d[2][1]} ")
  print(f"{list2d[0][2]} | {list2d[1][2]} | {list2d[2][0]} ")
  
list2d = [
         [num(),num(),num()],
         [num(),"BINGO",num()],
         [num(),num(),num()]
         ]

#printt()


############
numeric_elements = [item for sublist in list2d for item in sublist if isinstance(item, int)]

# Sort the numeric elements
numeric_elements.sort()

# Replace the sorted numeric elements back into the list
index = 0
for row in range(3):
    for col in range(3):
        if isinstance(list2d[row][col], int):
            list2d[row][col] = numeric_elements[index]
            index += 1

printt()