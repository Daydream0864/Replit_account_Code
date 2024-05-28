days = int(0)

print("30 days down, what you think?")

for i in range(1,31):
    days += 1
    answer = input(f"day {days}:")
    print()
    print(f"you thought day {days: <5} was {answer}")