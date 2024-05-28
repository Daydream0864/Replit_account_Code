while True:
  # Asking for inputs from users
  initials = input("Enter your three-letter initials: ")
  while len(initials) != 3 or not initials.isalpha():
    print("Invalid Initials! Please enter only three letters.")
    initials = input("Enter your three-letter initials: ")

  score = int(input("Enter your score out of 100,000: "))
  while score < 0 or score > 100_000:
    print("Invalid Score! Please enter a number between 0 and 100,000.")
    score = int(input("Enter your score out of 100,000: "))

  try:
    with open('high.scores', 'a') as f:
      f.write(f"{initials} {score}\n")
    print("\nScore saved successfully!\n")
  except Exception as e:
    print(f"\nAn error occurred while saving score: {e}")

  finish = input("Do you want to add more entries? (yes/no): ").lower()
  if finish == "no":
    break
print("Thank you!")