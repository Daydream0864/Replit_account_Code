beast = {
  "name" : None,
  "type" : None,
  "specail move" : None
}
print("MokéBeast")
print()
# mehr for loop lernen
#for name in beast.keys():
#  beast[name] = input(f"{name}: ").lower()

#print(beast[name])
#for name, type in beast.items():
#  if type == "water":
#    for key,value in beast.items():
#      print("\033[34m", end="")
#      print(f"{key}: {value} ")
#  elif type == "fire":
 #     for key,value in beast.items():
#        print("\033[32m", end="")
#        print(f"{key}: {value} ")
#  else:
 #   print("\033[33m", end="")

#for name, value in beast.items():
 # print(f"{name:<15}: {value}")


############


# Create a dictionary to store MokéBeast details
mokebeast = {}

# Ask user to input details
input_details = input("Enter details for your MokéBeast (name, type, special move, starting HP, starting MP): ")

# Split the input into individual details
details_list = input_details.split(", ")

# Assign details to dictionary keys
mokebeast["name"] = details_list[0]
mokebeast["type"] = details_list[1]
mokebeast["special_move"] = details_list[2]
mokebeast["starting_HP"] = int(details_list[3])
mokebeast["starting_MP"] = int(details_list[4])

# Output the beast's details
print("\033[91mMokéBeast Details:\033[0m")
for key, value in mokebeast.items():
    if key == "type":
        if value == "fire":
            print(f"\033[91m{key.capitalize()}: {value.capitalize()}\033[0m")
        elif value == "water":
            print(f"\033[94m{key.capitalize()}: {value.capitalize()}\033[0m")
        elif value == "air":
            print(f"\033[97m{key.capitalize()}: {value.capitalize()}\033[0m")
        else:
            print(f"{key.capitalize()}: {value.capitalize()}")
    else:
        print(f"\033[1m{key.capitalize()}: {value}\033[0m")