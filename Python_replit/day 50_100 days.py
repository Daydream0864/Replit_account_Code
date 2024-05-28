import random
import time

# Function to add an idea to my.ideas file
def add_idea():
    try:
        # Open my.ideas file in append mode
        with open("my.ideas", "a") as f:
            # Ask the user for their idea
            idea = input("Enter your idea: ")

            # Write the idea to the file
            f.write(f"{idea}\n")

            print("Idea added successfully!")

    except Exception as e:
        print(f"An error occurred while adding the idea: {e}")


# Function to load a random idea from my.ideas file
def load_random_idea():
    try:
        # Read all lines from my.ideas file
        with open("my.ideas", "r") as f:
            ideas = [line.strip() for line in f]

        if len(ideas) == 0:
            print("No ideas found.")
            return

        # Select a random idea
        selected_idea = random.choice(ideas)

        # Show the selected idea for a few seconds
        print(selected_idea)
        time.sleep(3)

    except FileNotFoundError:
        print("File not found. Make sure you have created a'my.ideas' file.")

    except Exception as e:
        print(f"An error occurred while reading the ideas: {e}")


# Main program loop
while True:
    # Print menu options
    print("\n--- Idea Storage System ---\n")
    print("[1] Add an idea")
    print("[2] Load random idea")
    print("[Q] Quit\n")

    # Get user's choice
    choice = input("Choose an option (1/2/Q): ").lower().strip()

    if choice == '1':
        add_idea()
    elif choice == '2':
        load_random_idea()
    elif choice == 'q':
        break
    else:
        print("Invalid choice. Please try again.\n")