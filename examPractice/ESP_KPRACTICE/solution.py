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
        
    
staff_members_under_or_over_a_given_amount_paid()

