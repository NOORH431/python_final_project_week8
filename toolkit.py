import random

# Welcoming start message
print("Welcome to your Personal Mini-Toolkit!")

# List to store tasks while the program runs
todo_list = []

# Main menu loop that keeps running until the user chooses to quit
while True:
    print("\n==============================")
    print("   PERSONAL MINI-TOOLKIT")
    print("==============================")
    print("1. To-Do List Manager")
    print("2. Simple Calculator")
    print("3. Number-Guessing Game")
    print("4. Quit")
    print("==============================")

    choice = input("Choose an option (1-4): ").strip()

    # ---------------------------------------------------------
    # TOOL 1: TO-DO LIST MANAGER
    # Lets the user add, view, and remove tasks from a list.
    # ---------------------------------------------------------
    if choice == "1":
        print("\n--- To-Do List Manager ---")
        while True:
            print("\nOptions: [1] View tasks  [2] Add task  [3] Remove task  [4] Back to main menu")
            todo_choice = input("What would you like to do? ").strip()

            if todo_choice == "1":
                if len(todo_list) == 0:
                    print("Your to-do list is currently empty!")
                else:
                    print("\nYour Tasks:")
                    for index, task in enumerate(todo_list, start=1):
                        print(f"  {index}. {task}")

            elif todo_choice == "2":
                new_task = input("Enter the new task: ").strip()
                if new_task:
                    todo_list.append(new_task)
                    print(f"Added '{new_task}' to your list!")
                else:
                    print("Task cannot be empty.")

            elif todo_choice == "3":
                if len(todo_list) == 0:
                    print("Nothing to remove — your list is empty.")
                else:
                    for index, task in enumerate(todo_list, start=1):
                        print(f"  {index}. {task}")
                    task_num = input("Enter the task number to remove: ").strip()
                    if task_num.isdigit() and 1 <= int(task_num) <= len(todo_list):
                        removed = todo_list.pop(int(task_num) - 1)
                        print(f"Completed and removed: '{removed}'")
                    else:
                        print("Invalid task number. Please try again.")

            elif todo_choice == "4":
                print("Returning to the main menu...")
                break
            else:
                print(f"'{todo_choice}' is not a valid option. Please enter 1, 2, 3, or 4.")

    # ---------------------------------------------------------
    # TOOL 2: SIMPLE CALCULATOR
    # Performs basic arithmetic (+, -, *, /) on two numbers.
    # ---------------------------------------------------------
    elif choice == "2":
        print("\n--- Simple Calculator ---")
        num1_input = input("Enter the first number: ").strip()
        operator = input("Choose an operation (+, -, *, /): ").strip()
        num2_input = input("Enter the second number: ").strip()

        # Check if inputs are valid numbers (supports decimals and negatives)
        try:
            num1 = float(num1_input)
            num2 = float(num2_input)

            if operator == "+":
                print(f"Result: {num1} + {num2} = {num1 + num2}")
            elif operator == "-":
                print(f"Result: {num1} - {num2} = {num1 - num2}")
            elif operator == "*":
                print(f"Result: {num1} * {num2} = {num1 * num2}")
            elif operator == "/":
                if num2 == 0:
                    print("Oops! You cannot divide by zero.")
                else:
                    print(f"Result: {num1} / {num2} = {num1 / num2:.2f}")
            else:
                print(f"'{operator}' is not a supported operator. Please use +, -, *, or /.")
        except ValueError:
            print("Invalid input! Please make sure you enter valid numbers.")

    # ---------------------------------------------------------
    # TOOL 3: NUMBER-GUESSING GAME
    # Generates a secret number (1-20) and gives hints until guessed.
    # ---------------------------------------------------------
    elif choice == "3":
        print("\n--- Number-Guessing Game ---")
        secret_number = random.randint(1, 20)
        attempts = 0
        print("I am thinking of a number between 1 and 20. Can you guess it?")

        while True:
            guess_input = input("Enter your guess: ").strip()

            if not guess_input.isdigit():
                print("Please enter a whole number between 1 and 20.")
                continue

            guess = int(guess_input)
            attempts += 1

            if guess < 1 or guess > 20:
                print("Out of range! Stay between 1 and 20.")
            elif guess < secret_number:
                print(f"{guess} is too low! Try again.")
            elif guess > secret_number:
                print(f"{guess} is too high! Try again.")
            else:
                print(f"Spot on! You guessed {secret_number} in {attempts} tries!")
                break

    # ---------------------------------------------------------
    # QUIT OPTION
    # ---------------------------------------------------------
    elif choice == "4":
        print("\nThanks for using the Personal Mini-Toolkit. Goodbye!")
        break

    # ---------------------------------------------------------
    # INVALID MENU CHOICE HANDLER
    # ---------------------------------------------------------
    else:
        print(f"\nSorry, '{choice}' is not on the menu. Please enter 1, 2, 3, or 4.")
