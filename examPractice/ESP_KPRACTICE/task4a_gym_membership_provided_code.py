import pandas as pd
import matplotlib.pyplot as plt

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

def staff_members_under_or_over_a_given_amount_paid():
    df = pd.read_csv("Task_4a.csv")
    grouped_filter = df.groupby('Member Name')['Amount Paid'].sum().reset_index()
    #print(df)
    is_valid = True
    
    while is_valid:
        try:
            print("\n##### Select an Option #####")
            print("### 1. View staffs over a given amount")
            print("### 2. View staffs under a given amount")
            user_input_option = input("=> ")
            
            if user_input_option not in {'1', '2'}:
                print('\nInvalid option selected, please try again')
            else:
                if user_input_option == '1':
                    user_given_amount = int(input("\nEnter a given amount: £"))
                    amount_paid_filter = grouped_filter.loc[grouped_filter['Amount Paid'] > user_given_amount]
                    if amount_paid_filter.empty:
                        print('We cannot find results matching your criteria')
                    else:
                        plot_staff_members_under_or_over_a_given_amount_paid(amount_paid_filter, f"The trends and patterns over time for staff members over £{user_given_amount}")
                        print(f"\nThe staff members paid over £{user_given_amount} are:\n{amount_paid_filter.iloc[:, 0].to_string(index=False)}")
                        is_valid = False 
                else:
                    user_given_amount = int(input("\nEnter a given amount: £"))
                    amount_paid_filter = grouped_filter.loc[grouped_filter['Amount Paid'] < user_given_amount]
                    if amount_paid_filter.empty:
                        print('Data frame is empty')
                    else:
                        plot_staff_members_under_or_over_a_given_amount_paid(amount_paid_filter, f"The trends and patterns over time for staff members under £{user_given_amount}")
                        print(f"\nThe staff members paid under £{user_given_amount} are:\n{amount_paid_filter.iloc[:, 0].to_string(index=False)}")
                        is_valid = False
                        
        except ValueError:
            print('Only Numbers are accepted')


def plot_staff_members_under_or_over_a_given_amount_paid(filtered_data,title):
    plt.figure(figsize=(10,6))
    bars = plt.bar(filtered_data['Member Name'], filtered_data['Amount Paid'])
    plt.bar_label(bars, fmt='£%.2f', fontsize=8)
    plt.xlabel('Member Name')
    plt.ylabel('Amount Paid')
    plt.title(title)
    plt.show()


def total_visits_per_month_for_all_membership_types():
    df = pd.read_csv("Task_4a.csv")
    
    membership_and_visits_filter = df.groupby('Membership Type').agg(
    {
        'Visits per Month' : 'sum'
    })
    print(f"The total visits per month for all membership type is: \n\n{membership_and_visits_filter}")
    plot_total_visits_per_month_for_all_membership_types(membership_and_visits_filter.reset_index())
    

def plot_total_visits_per_month_for_all_membership_types(data):
   bars = plt.bar(data['Membership Type'], data['Visits per Month'], color='skyblue', edgecolor='black')
   plt.bar_label(bars, fontsize=8)
   plt.xlabel('Membership Type')
   plt.ylabel('Visits per Month')
   plt.title('Total visits per month for all membership types')
   plt.show()


def income_for_various_membership_types():
    df = pd.read_csv("Task_4a.csv")
    
    income_membership_filter = df.groupby('Membership Type').agg({'Amount Paid' : 'sum'})
    print(f"The total income for various membership type is: \n\n{income_membership_filter}")
    plot_income_for_various_membership_types(income_membership_filter.reset_index())
    
def plot_income_for_various_membership_types(data):
    bars = plt.bar(data['Membership Type'], data['Amount Paid'], color='skyblue', edgecolor='black')
    plt.bar_label(bars, fmt='£%.2f', fontsize=8)
    plt.xlabel('Membership Type')
    plt.ylabel('Amount Paid(£)')
    plt.title('Income for various membership types')
    plt.show()

    

# Function 4: Main menu
def main_menu():
    while True:
        print("\n=== Gym Staff Payment System ===")
        print("0. Exit")
        print("1. Find total amount paid for a staff member")
        print("2. View Staff members under or over a given amount paid")
        print("3. Get the Total visits per month for all membership types")
        print("4. View the income for various membership types")
        print("5. View different members signup date")
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
        
        elif option == "2":
            staff_members_under_or_over_a_given_amount_paid()
            
        elif option == "3":
            total_visits_per_month_for_all_membership_types()
            
        elif option == "4":
            income_for_various_membership_types()
        
        elif option == "5":
            different_members_signup_date()
        
        else:
            print("Invalid option. Try again.")

main_menu()
