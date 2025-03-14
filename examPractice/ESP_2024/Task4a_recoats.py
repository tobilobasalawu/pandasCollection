import pandas as pd

# Outputs the initial menu and checks validates the input
def main_menu():
    flag = True

    while flag:

        print("####################################################")
        print("############## Recoats Adventure Park ##############")
        print("####################################################")
        print("")
        print("########### Please select an option ################")
        print("### 1. Total income by source")
        print(' ')

        choice = input('Enter your number selection here: ')

        try:
            int(choice)
        except:
            print("Sorry, you did not enter a valid option")
            print(' ')
            flag = True
        else:    
            print('Choice accepted!')
            flag = False

    return choice

# Submenu for totals, provides type check validation for the input
def total_menu ():
    flag = True

    while flag:
        print(' ')
        print("####################################################")
        print("############## Total income by source ##############")
        print("####################################################")
        print("")
        print("########## Please select an income source ##########")
        print("### 1. Tickets")   
        print("### 2. Gift Shop") 
        print("### 3. Snack Stand")  
        print("### 4. Pictures")

        choice = input('Enter your number selction here: ')

        try:
            int(choice)
        except:
            print("Sorry, you did not enter a valid option")
            print(' ')
            flag = True
        else:    
            print('\nChoice accepted!')
            flag = False

    return choice   

# takes the total submenu input and converts the number to a string of the source name
def convert_total_men_coice(total_men_choice):
    
    if total_men_choice == "1":
        tot_choice = "Tickets"
    elif total_men_choice == "2":
        tot_choice = "Gift Shop"
    elif total_men_choice == "3":
        tot_choice= "Snack Stand"
    else:
        tot_choice = "Pictures"  
    
    return tot_choice

# creates a new dataframe with the selected income source then creates a total row
# outputs the final total in a message
def get_total_data(total_choice):
    
    df = pd.read_csv("Task4a_data.csv")
    
    income = df[["Day", total_choice]]

    total = income[total_choice].sum()

    msg = "The total income from {} was: £{}".format(total_choice, total)
    return msg

def different_payment_types_and_income_sources():
    df = pd.read_csv("Task4a_data.csv")

    different_payment_types_and_income_sources_values = df.groupby('Pay Type').agg({
        'Tickets': 'sum',
        'Gift Shop': 'sum',
        'Snack Stand': 'sum',
        'Pictures': 'sum'
    })

    print('The different payment types and income sources over time is: \n')
    print(different_payment_types_and_income_sources_values)

def income_on_different_days_of_the_week():
    df = pd.read_csv("Task4a_data.csv")

    income_sources_on_different_days_values = df.groupby('Day').agg({
        'Tickets' : 'sum',
        'Gift Shop' : 'sum',
        'Snack Stand' : 'sum',
        'Pictures' : 'sum'
    })

    income_sources_on_different_days_values['Total'] = income_sources_on_different_days_values.sum(axis=1)

    print('The income on the different days of the week over time is: \n')
    print(income_sources_on_different_days_values)

main_menu_choice = main_menu()
if main_menu_choice == "1":
    total_men_choice = total_menu()
    total_choice = convert_total_men_coice(total_men_choice)
    print(get_total_data(total_choice))
