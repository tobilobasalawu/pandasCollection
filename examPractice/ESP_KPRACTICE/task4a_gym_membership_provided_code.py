import pandas as pd

# Function 1: Read CSV and get total amount paid for a staff member
def get_total_paid_for_member():
    df = pd.read_csv("Task_4a.csv")
    is_valid = True
    
    while is_valid:
        members_df = df['Member Name'].unique()
        members_name_dict = {str(i+1): name for i,name in enumerate(members_df)}
        for key, values in members_name_dict.items():
            print(f"{key}. {values}")
            
        choice = input("\nEnter the number of the staff member: ")
        if choice not in members_name_dict:
            print('Invalid Input, try again\n')
        else:
            filtered = df[df["Member Name"] == members_name_dict[choice]]
            total_paid = filtered["Amount Paid"].sum()
            print((f"\nTotal amount paid for {members_name_dict[choice]}: £{total_paid:.2f}"))
            is_valid = False
    

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
                    print(f"\nThe staff members paid over £{user_given_amount} are:\n{amount_paid_filter.iloc[:, 0].to_string(index=False)}")
                    is_valid = False 
                else:
                    user_given_amount = int(input("\nEnter a given amount: £"))
                    amount_paid_filter = grouped_filter.loc[grouped_filter['Amount Paid'] < user_given_amount]
                    print(f"\nThe staff members paid under £{user_given_amount} are:\n{amount_paid_filter.iloc[:, 0].to_string(index=False)}")
                    is_valid = False
        except ValueError:
            print('Only numbers are accepted')



def total_visits_per_month_for_all_membership_types():
    df = pd.read_csv("Task_4a.csv")
    
    membership_and_visits_filter = df.groupby('Membership Type').agg(
    {
        'Visits per Month' : 'sum'
    })
    print(f"\nThe total visits per month for all membership type is: \n\n{membership_and_visits_filter}")
    


def income_for_various_membership_types():
    df = pd.read_csv("Task_4a.csv")
    
    
    income_membership_filter = df.groupby('Membership Type').agg({'Amount Paid' : 'sum'})
    print(f"\nThe total income for various membership type is: \n\n{income_membership_filter}")
    

def different_members_signup_date():
    df = pd.read_csv("Task_4a.csv")
    is_valid = True
    
    while is_valid:
        members_df = df['Member Name'].unique()
        members = {str(i+1): name for i,name in enumerate(members_df)}
        for key,values in members.items():
            print(f"## {key}. {values}")
        user_member_option = input('\nPlease select a member to view their sign up date: ')
        
        if user_member_option not in members:
            print('Invalid option, please try again\n')
        else:
            members_signup_date_filter = df.loc[df['Member Name'] == members[user_member_option], 'Sign-Up Date']
            print(f"\nThe sign up date for {members[user_member_option]} is: \n{members_signup_date_filter.to_string(index=False)}")
            is_valid = False

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
            get_total_paid_for_member()
            
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
