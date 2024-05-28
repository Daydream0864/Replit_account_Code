website = {"name": None, "url": None, "desc": None, "rating": None}

for name in website.keys():
  website[name] = input(f"{name}: ")

print(website[name])
for name, value in website.items():
  print(f"{name}: {value}")

# 