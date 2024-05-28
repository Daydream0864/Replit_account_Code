import os, time
def add_todo(todo_list):
  description = input("Enter the description: ")
  due_date = input("Enter the due date: ")
  priority = input("Enter the priority (high, medium, or low): ").lower()
  if priority == "high" or priority == "medium" or priority == "low":
    todo_list.append({
      "description": description,
      "due_date": due_date,
      "priority": priority
    })
    print(f"'{description}' added to the to-do list.")
  else:
    print(f"sorry not a correct input,{priority}. END")


def view_all(todo_list):
  print("All To-Dos:")
  for i, todo in enumerate(todo_list, start=1):
    print(
      f"{i}. Description: {todo['description']}, Due Date: {todo['due_date']}, Priority: {todo['priority']}"
    )


def view_priority(todo_list, priority):
  print(f"To-Dos with Priority '{priority}':")
  for i, todo in enumerate(todo_list, start=1):
    if todo['priority'] == priority:
      print(
        f"{i}. Description: {todo['description']}, Due Date: {todo['due_date']}"
      )


def edit_todo(todo_list, index):
  if 1 <= index <= len(todo_list):
    todo = todo_list[index - 1]
    description = input("Enter the new description: ")
    due_date = input("Enter the new due date: ")
    priority = input("Enter the new priority (high, medium, or low): ")
    todo['description'] = description
    todo['due_date'] = due_date
    todo['priority'] = priority
    print(f"To-Do at index {index} updated.")
  else:
    print(f"Invalid index. No To-Do found at index {index}.")


def remove_todo(todo_list, index):
  if 1 <= index <= len(todo_list):
    removed_todo = todo_list.pop(index - 1)
    print(f"'{removed_todo['description']}' removed from the to-do list.")
  else:
    print(f"Invalid index. No To-Do found at index {index}.")


def clear(timeq):
  time.sleep(timeq)
  os.system("clear")


def main():
  todo_list = []

  while True:
    print("\nMenu:")
    print("1. Add a To-Do")
    print("2. View all To-Dos")
    print("3. View To-Dos by Priority")
    print("4. Edit a To-Do")
    print("5. Remove a To-Do")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
      add_todo(todo_list)
      clear(1)
    elif choice == "2":
      view_all(todo_list)
      clear(3)
    elif choice == "3":
      priority = input("Enter the priority to filter (high, medium, or low): ")
      view_priority(todo_list, priority)
      clear(3)
    elif choice == "4":
      index = int(input("Enter the index of the To-Do to edit: "))
      edit_todo(todo_list, index)
      clear(1)
    elif choice == "5":
      index = int(input("Enter the index of the To-Do to remove: "))
      remove_todo(todo_list, index)
    elif choice == "6":
      print("Exiting the program.")
      break
    else:
      print("Invalid choice. Please try again.")


if __name__ == "__main__":
  main()
