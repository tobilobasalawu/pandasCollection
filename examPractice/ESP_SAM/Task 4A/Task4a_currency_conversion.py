import pandas as pd
import matplotlib.pyplot as plt

def menu():
    '''
    The function generates the UI the accepts and validates user choice
    :return:
        menu_choice - the users selected choice form the menu
    '''

    flag = True

    while flag:
        print("######################################################")
        print("Which conversion would you like to make today?")
        print("1. Pound Sterling (GBP) to Euros (EUR)")
        print("2. Euros (EUR) to Pound Sterling(GBP)")
        print("3. Pound (GBP) to Austrailan Dollars (AUD)")
        print("4. Austrailan Dollars (AUD) to Pound Sterling (GBP)")
        print("5. Pound Sterling (GBP) to Japanese Yen (JPY)")
        print("6. Japanese Yen (JPY) to Pound Sterling (GBP)")
        print("7. Pound Sterling (GBP) to US Dollar (USD)")
        print("8. US Dollar (USD) to Pound Sterling (GBP)")
        print(' ')
        print("######################################################")

        
        menu_choice = input("Please enter the number of your choice (1-6): ")
        print(' ')

        try:
            int(menu_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(menu_choice) < 1 or int(menu_choice) > 8:
                print("Sorry, you did not enter a valid choice")
                flag = True
            else:
                return menu_choice  

def get_currency (menu_choice):
    '''
    Gets the short version of the conversion information based on user menu choice
    :param menu_choice: The selected choice from the conversion menu
    :return: currency - converts the users selected choice to the currency column name in the csv file
    '''

    currencies = {
        '1': 'GBP - EUR',
        '2': 'EUR - GBP',
        '3': 'GBP - AUD',
        '4': 'AUD - GBP',
        '5': 'GPB - JPY',
        '6': 'JPY - GBP',
        '7': 'GBP - USD',
        '8': 'USD - GBP'
    }
   
    currency = currencies.get(menu_choice)
    
    return currency


def get_conversion_rate(currency):
    '''
    The get_conversion_rate function uses pandas to get the latest conversion rate
    Imports a csv file in to a data frame
    Uses 'iloc' to get the last/most recent value in the selected column
    :param currency: gets the currency column name
    :return: conversion rate - gets the value at the end of the column(latest value)
    '''

    try:
        df = pd.read_csv("Task4a_data.csv")
    except FileNotFoundError:
        print('The Data file cannot be found')
    
    conversion_rate = round(df[currency].iloc[-1],2)
    return conversion_rate

def get_amount_to_convert(currency):
    '''
    Accepts and validates user input for the amount they want to convert
    :param currency: gets the currency column name
    :return: conversion_amount - the amount the user wish to convert
    '''

    print("You are converting: ",currency)

    flag = True
    
    while flag:
        conversion_amount = input("Please enter the amount you wish to convert: ")
        try:
            float(conversion_amount)
        except:
            print(' ')
            print("Sorry, you must enter a numerical value")
            flag = True
        else:
            return conversion_amount  

def perfom_conversion(conversion_amount, conversion_rate, currency):
    '''
    Performs the converison and outputs the final values
    :param conversion_amount: the amount the user wish to convert
    :param conversion_rate: the value at the end of the column(latest value)
    :param currency: the currency column name in the csv file also known as the user selected currency conversion
    :return: prints out the converted amount to the user
    '''

    amount_recieved = round(conversion_amount * conversion_rate, 2)

    print(' ')
    print("##################################")
    print('You are converting {} in {}'.format(conversion_amount, currency[0:3]) )
    print('You will receive {} in {}'.format(amount_recieved, currency[6:9]))


def value_of_the_pound_GBP_to_the_US_dollar_USD(days):
    '''
    the value_of_the_pound_GBP_to_the_US_dollar_USD function uses pandas to gets the
    latest values of the latest rate based on the number of days selected by the user
    :param days: the number of days selected by the user
    :return: GBP_US_column - the column of the selected conversion
    '''
    try:
        df = pd.read_csv("Task4a_data.csv")
    except FileNotFoundError:
        print('The Data file cannot be found')
    GBP_US_column = df.iloc[-days:, 7]
    print(f'The values from GBP to USD for the last {days} days is:\n{GBP_US_column.to_string(index=False)}')

    return GBP_US_column

def value_of_the_US_dollar_USD_to_the_pound_GBP(days):
    '''
    the value_of_the_US_dollar_USD_to_the_pound_GBP function uses pandas to gets the
    latest values of the latest rate based on the number of days selected by the user
    :param days: the number of days selected by the user
    :return: US_GBP_column - the column of the selected conversion
    '''

    try:
        df = pd.read_csv("Task4a_data.csv")
    except FileNotFoundError:
        print('The Data file cannot be found')
    US_GBP_column = df.iloc[-days:, -1]
    print(f'The values from USD to GBP for the last {days} days is:\n{US_GBP_column.to_string(index=False)}')

    return US_GBP_column

def visualize_trends(column, days):
    '''
    The visualize_trends function displays graphical/diagrammatic representation of the column of the selected conversion using matplotlib
    :param column: the column of the selected conversion
    :param days: the number of days selected by the user
    :return: a line graph display the latest values for the selected days
    '''
    plt.figure(figsize=(10, 5))
    plt.plot(column)
    plt.title(f'The values from GBP to USD for the last {days} days')
    plt.xlabel('Days')
    plt.ylabel('Amount')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

def trends_and_patterns_overtime_menu():
    '''
    The trends_and_patterns_overtime_menu function handles the menu for the trends and patterns section
    :return: displays the column and graph for the user selected choice
    '''
    print("######################################################")
    print("Which Trends and patterns overtime would you like to view?\n1. The value of the pound (GBP) to the US dollar (USD) \n2. The value of the US Dollar (USD) to the pound (GBP). ")
    print('\n######################################################')

    flag = True

    while flag:
        try:
            userInput = int(input('Select an option from the trends and patterns menu: '))
            print(' ')

            if userInput == 1:
                daysInput = int(
                    input('The enter the number of days(time) of the trends and patterns you would like to view (within 86 days): '))
                if daysInput < 1 or daysInput > 86:
                    print('Days must be between 1 and 86')
                else:
                    GBP_US_column = value_of_the_pound_GBP_to_the_US_dollar_USD(daysInput)
                    visualize_trends(GBP_US_column, daysInput)
                    flag = False

            elif userInput == 2:
                daysInput2 = int(
                    input('The enter the number of days(time) of the trends and patterns you would like to view: '))
                if daysInput2 < 1 or daysInput2 > 86:
                    print('Days must be between 1 and 86')
                else:
                    US_GBP_column = value_of_the_US_dollar_USD_to_the_pound_GBP(daysInput2)
                    visualize_trends(US_GBP_column, daysInput2)
                    flag = False

            else:
                print('You have selected an InValid Option Try again\n')
                flag = True
        except:
            print('Please only numerical values are accepted.\n')


def execute_program():
    '''
    Executes/Runs the entire program
    '''

    flag = True

    while flag:
        print("######################################################")
        print("Select a Category to continue")
        print("1. Convert Currencies\n2. View Trends and patterns over time for selected currencies")
        print('\n######################################################')

        userInput = input('Select an option: ')

        if userInput.isdigit() and userInput in {'1', '2'}:
            print('Choice Accepted\n')
            flag = False
            if userInput == '1':
                menu_choice = menu()
                currency = get_currency(menu_choice)
                conversion_rate = get_conversion_rate(currency)
                conversion_amount = float(get_amount_to_convert(currency))
                perfom_conversion(conversion_amount, conversion_rate, currency)
            else:
                trends_and_patterns_overtime_menu()
        else:
            print('You have selected an Invalid choice')
            flag = True

execute_program()

