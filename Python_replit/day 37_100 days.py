print("🌟Star Wars Name Generator🌟")


firstname = input("Input your first name > ").title()
lastname = input("Input your lastname > ").lower()
mumsname = input("Input your mother's maiden name > ").title()
cityborn = input("Input the city where you were born > ").lower()

sliceone = firstname[:3]
slicetwo = lastname[:3]

slicethree = mumsname[:2]
slicefour = cityborn[4:]

Star_Wars_first_name = f"{sliceone}{slicetwo}"
Star_Wars_last_name = f"{slicethree}{slicefour}"
print(Star_Wars_first_name, Star_Wars_last_name)


###############
print("STAR WARS NAME GENERATOR")

all = input("Enter your first name, last name, Mum's maiden name and the city you were born in").split()

first = all[0].strip()
last = all[1].strip()
maiden = all[2].strip()
city = all[3].strip()

name = f"{first[:3].title()}{last[:3].lower()} {maiden[:2].title()}{city[-3:].lower()}"

print(f"Your Star Wars name is {name}")