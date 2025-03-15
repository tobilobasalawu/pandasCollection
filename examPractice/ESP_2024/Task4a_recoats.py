import pandas as pd
import matplotlib.pyplot as plt


# Outputs the initial menu and checks validates the input
def main_menu():
    flag = True

    while flag:

        print("\n####################################################")
        print("############## Recoats Adventure Park ##############")
        print("####################################################")
        print("########### Please select an option ################")
        print("### 1. Total income by source")
        print("### 2. View the different payment types and income sources")
        print("### 3. View the income on different days of the week\n")

        choice = input('Enter your number selection here: ')

        try:
            int(choice)
        except:
            print("Sorry, you did not enter a valid option\n")
            flag = True
        else:
            flag = False

    return choice


# Submenu for totals, provides type check validation for the input
def get_total_menu_and_total_choice ():
    flag = True

    while flag:
        choice_object = {
            '1': 'Tickets',
            '2': 'Gift Shop',
            '3': 'Snack Stand',
            '4': 'Pictures'
        }

        print("\n############## Total income by source ##############")
        print("####################################################")
        print("########## Please select an income source ##########")
        for key,values in choice_object.items():
            print(f"{key} : {values}")

        choice = input('\nEnter your number selection here: ')
        if choice in choice_object:
            flag = False
            return choice_object[choice]

        else:
            print('The option you selected is not valid, Please Try Again')


# creates a new dataframe with the selected income source then creates a total row
# outputs the final total in a message
def get_total_data(total_choice):
    try:
        df = pd.read_csv("Task4a_data.csv")
    except FileNotFoundError:
        print('The data File cannot be found')

    income = df[["Day", total_choice]]
    total = income[total_choice].sum()
    msg = "The total income from {} was: £{}".format(total_choice, total)

    return msg


def different_payment_types_and_income_sources():
    try:
        df = pd.read_csv("Task4a_data.csv")
    except FileNotFoundError:
        print('The data File cannot be found')

    different_payment_types_and_income_sources_values = df.groupby('Pay Type').agg({
        'Tickets': 'sum',
        'Gift Shop': 'sum',
        'Snack Stand': 'sum',
        'Pictures': 'sum'
    })

    flag = True

    while flag:
        user_payment_type_input = input("\nEnter the Payment type you would view (card or cash): ").capitalize()
        if user_payment_type_input in {'Card', 'Cash'}:

            if user_payment_type_input.capitalize() == 'Card':
                print(f"\nThe income source for {user_payment_type_input} overtime is:")
                print(different_payment_types_and_income_sources_values.iloc[0])

                plt.figure(figsize=(10, 6))
                plt.pie(different_payment_types_and_income_sources_values.iloc[0], autopct="%1.1f%%")
                plt.title(f'Income sources for {user_payment_type_input} overtime')
                plt.legend(different_payment_types_and_income_sources_values.columns)
                plt.show()

            else:
                print(f"\nThe income source for {user_payment_type_input} overtime is:")
                print(different_payment_types_and_income_sources_values.iloc[1])

                plt.figure(figsize=(10, 6))
                plt.pie(different_payment_types_and_income_sources_values.iloc[1], autopct="%1.1f%%")
                plt.title(f'Income sources for {user_payment_type_input} overtime')
                plt.legend(different_payment_types_and_income_sources_values.columns)
                plt.show()

            flag = False
        else:
            print('The Payment type you entered is not valid, Try Again!\n')


def income_on_different_days_of_the_week():
    try:
        df = pd.read_csv("Task4a_data.csv")
    except FileNotFoundError:
        print('The data File cannot be found')

    income_sources_on_different_days_values = df.groupby('Day').agg({
        'Tickets' : 'sum',
        'Gift Shop' : 'sum',
        'Snack Stand' : 'sum',
        'Pictures' : 'sum'
    })

    income_sources_on_different_days_values['Total'] = income_sources_on_different_days_values.sum(axis=1)
    income_sources_on_different_days_values = income_sources_on_different_days_values.reset_index()

    print('\nThe income on the different days of the week over time is:')
    print(income_sources_on_different_days_values.to_string(index=False))

    plt.figure(figsize=(10,7))
    plt.xticks(rotation=45)
    plt.title('Income on different days of the week')
    plt.xlabel('Days')
    plt.ylabel('Total Income')
    plt.bar(income_sources_on_different_days_values['Day'], income_sources_on_different_days_values['Total'], color = 'skyblue', edgecolor = 'black')
    plt.show()


def execute_main_program():
    flag = True

    while flag:
        main_menu_choice = main_menu()

        if main_menu_choice == "1":
            total_men_choice = get_total_menu_and_total_choice()
            print(get_total_data(total_men_choice))
            flag = False
        elif main_menu_choice == "2":
            different_payment_types_and_income_sources()
            flag = False
        elif main_menu_choice == "3":
            income_on_different_days_of_the_week()
            flag = False
        else:
            print('The choice you selected is not in the menu, Try Again!')

execute_main_program()