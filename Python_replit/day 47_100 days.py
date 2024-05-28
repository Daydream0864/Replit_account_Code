import random

# Define the 2D dictionary
#teachers = {
#  "Teacher1": {
#    "Intelligence": random.randint(1, 10),
#    "Handsomness": 75,
#    "L33t c0ding skillz": 85,
#    "Baldness level": 20
#  },
#  "Teacher2": {
#    "Intelligence": random.randint(1, 10),
#    "Handsomness": 80,
#    "L33t c0ding skillz": 90,
#    "Baldness level": 50
#  }
#}
#
#
#def add_teacher(teachers, name, intelligence, handsomeness, coding_skills,
#                baldness_level):
#  teachers[name] = {
#    "Intelligence": intelligence,
#    "Handsomness": handsomeness,
#    "L33t c0ding skillz": coding_skills,
#    "Baldness level": baldness_level
#  }
#
#
#add_teacher(teachers, "Teacher1", 90, 75, 85, 20)
#while True:
#  # Get the user to pick one of the two cards
#  chosen_teacher = input("Choose a teacher (Teacher1 or Teacher2): ")
#  if chosen_teacher not in teachers:
#    print("Invalid teacher. Please choose either Teacher1 or Teacher2.")
#    continue

  # Get the user to pick a stat from that card
#  chosen_stat = input(
 #   "Choose a stat (Intelligence, Handsomness, L33t c0ding skillz, Baldness #level): "
#  )
#  if chosen_stat not in teachers[chosen_teacher]:
#    print(
#      "Invalid stat. Please choose either Intelligence, Handsomness, L33t #c0ding skillz, or Baldness level."
#    )
#    continue
#
#  # Display the chosen stat for both cards
#  print(
#    f"{chosen_teacher}'s {chosen_stat}: {teachers[chosen_teacher]#[chosen_stat]}"
#  )
#  print(
#    f"{'Teacher1' if chosen_teacher == 'Teacher2' else 'Teacher2'}'s #{chosen_stat}: {teachers['Teacher1' if chosen_teacher == 'Teacher2' else #'Teacher2'][chosen_stat]}"
#  )
#
#  # Output which has won
#  if teachers[chosen_teacher][chosen_stat] > teachers[
#      'Teacher1' if chosen_teacher == 'Teacher2' else 'Teacher2']#[chosen_stat]:
#    print(f"{chosen_teacher} wins!")
#    again = input("y/n").lower()
#    if again == "y":
#      continue
#
#  else:
#    print(
#      f"{'Teacher1' if chosen_teacher == 'Teacher2' else 'Teacher2'} wins!")
################################

def add_teacher(teachers, name, intelligence, handsomeness, coding_skills, baldness_level):
  teachers[name] = {
      "Intelligence": intelligence,
      "Handsomness": handsomeness,
      "L33t c0ding skillz": coding_skills,
      "Baldness level": baldness_level
  }

# Initialize an empty dictionary
teachers = {}

while True:
  # Ask the user if they want to add a new teacher
  add_new_teacher = input("Do you want to add a new teacher? (yes/no): ")
  if add_new_teacher.lower() == "yes":
      name = input("Enter the name of the teacher: ")
      intelligence = int(input("Enter the Intelligence of the teacher: "))
      handsomeness = int(input("Enter the Handsomeness of the teacher: "))
      coding_skills = int(input("Enter the L33t c0ding skillz of the teacher: "))
      baldness_level = int(input("Enter the Baldness level of the teacher: "))
      add_teacher(teachers, name, intelligence, handsomeness, coding_skills, baldness_level)
      print(f"Added {name} to the game.")
      continue

  # Get the user to pick one of the cards
  chosen_teacher = input("Choose a teacher: " + ', '.join(teachers.keys()) + ": ")
  if chosen_teacher not in teachers:
      print("Invalid teacher. Please choose from the following: " + ', '.join(teachers.keys()))
      continue

  # Get the user to pick a stat from that card
  chosen_stat = input("Choose a stat (Intelligence, Handsomness, L33t c0ding skillz, Baldness level): ")
  if chosen_stat not in teachers[chosen_teacher]:
      print("Invalid stat. Please choose either Intelligence, Handsomness, L33t c0ding skillz, or Baldness level.")
      continue

  # Display the chosen stat for all cards
  for teacher in teachers:
      print(f"{teacher}'s {chosen_stat}: {teachers[teacher][chosen_stat]}")

  # Output which has won
  winner = max(teachers, key=lambda x: teachers[x][chosen_stat])
  print(f"{winner} wins!")
