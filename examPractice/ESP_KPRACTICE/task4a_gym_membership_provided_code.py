import pandas as pd

# Function 1: Read CSV and get total amount paid for a staff member
def get_total_paid_for_member(member_name):
    df = pd.read_csv("Task_4a.csv")
    filtered = df[df["Member Name"] == member_name]
    total_paid = filtered["Amount Paid"].sum()
    return total_paid

# Function 2: Display numbered list of unique names, and get user input
def get_user_selection(names):
    print("\nSelect a staff member:\n")
    for i, name in enumerate(names, start=1):
        print(f"{i}. {name}")
    while True:
        try:
            choice = int(input("\nEnter the number of the staff member: "))
            if 1 <= choice <= len(names):
                return choice
            else:
                print("Invalid number. Try again.")
        except ValueError:
            print("Please enter a valid number.")

# Function 3: Convert number to name
def get_name_from_number(number, names):
    return names[number - 1]

# Function 4: Main menu
def main_menu():
    print("=== Gym Staff Payment System ===")
    print("1. Find total amount paid for a staff member")
    print("0. Exit")

    while True:
        option = input("\nSelect an option: ")
        if option == "1":
            df = pd.read_csv("Task_4a.csv")
            unique_names = sorted(df["Member Name"].unique())
            number = get_user_selection(unique_names)
            name = get_name_from_number(number, unique_names)
            total = get_total_paid_for_member(name)
            print(f"\nTotal amount paid for {name}: £{total:.2f}")
        elif option == "0":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

main_menu()