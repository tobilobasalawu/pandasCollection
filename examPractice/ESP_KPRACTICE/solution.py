import pandas as pd

def staff_members_under_or_over_a_given_amount_paid():
    df = pd.read_csv("Task_4a.csv")
    grouped_filter = df.groupby('Member Name')['Amount Paid'].sum().reset_index()
    #print(df)
    is_valid = True
    
    while is_valid:
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



def total_visits_per_month_for_all_membership_types():
    df = pd.read_csv("Task_4a.csv")
    
    membership_and_visits_filter = df.groupby('Membership Type').agg(
    {
        'Visits per Month' : 'sum'
    })
    print(f"The total visits per month for all membership type is: \n\n{membership_and_visits_filter}")
    


def income_for_various_membership_types():
    df = pd.read_csv("Task_4a.csv")
    
    
    income_membership_filter = df.groupby('Membership Type').agg({'Amount Paid' : 'sum'})
    print(f"The total income for various membership type is: \n\n{income_membership_filter}")
    

def different_members_signup_date():
    df = pd.read_csv("Task_4a.csv")
    
    members = {'1': 'Chris Evans', '2' : 'Jane Smith', '3' : 'John Doe', '4' : 'Laura Kim', '5' : 'Lisa Ray', '6' : 'Michael Chan', '7' : 'Sarah Lee', '8': 'Tom Allen'}
    for key,values in members.items():
        print(f"## {key}. {values}")
    user_member_option = input('\nPlease select a member to view their sign up date: ')
    
    if user_member_option not in members:
        print('Invalid option, please try again')
    else:
        members_signup_date_filter = df.loc[df['Member Name'] == members[user_member_option], 'Sign-Up Date']
        print(f"\nThe sign up date for {members[user_member_option]} is: \n{members_signup_date_filter.to_string(index=False)}")

different_members_signup_date()




