import pandas as pd #Importing data handling library

def main_menu():

    '''
    The main menu - that is first displayed to the user and prompts the user for a choice
    :returns:
        str: The user choice
    '''

    flag = True

    while flag:

        print("#################################################")
        print("#### Welcome to Elanp Air Flight Data system ####")
        print("#################################################")
        print("")
        print("########### Please select an option #############")
        print("### 1. View passenger numbers")
        print("### 2. View AM and PM flights for two selected routes")
        print("### 3. Departure airport that has the most passengers over time.")
        print(' ')

        choice = input('Enter your number selection here: ')

        try:
            int(choice)
        except:
            print("Sorry, you did not enter a valid option")
            print('')
            flag = True
        else:
            flag = False

    return choice

#
def get_depart():
    '''
       Handles the users input for departure Airport - user enters a choice
       :returns:
           str: The user choice
       '''

    flag = True

    while flag:

        print("########### Please select departure airport #############")
        print("### 1. Dublin (DUB)")
        print("### 2. Edinburgh (EDI)")
        print("### 3. Glasgow (GLA")
        print("### 4. London Heathrow (LHR)")
        print("### 5. London Luton (LTN)")
        print("### 6. Manchester (MAN)")
        print(' ')

        choice = input('Enter your number selection here: ')

        try:
            int(choice)
        except:
            print("Sorry, you did not enter a valid option")
            print('')
            flag = True
        else:
            flag = False

    return choice


def get_destination(depart):
    '''
       Handles the users input for destination Airport - user enters a choice
       :returns:
           str: The user choice
       '''

    flag = True

    while flag:

        print("########### Please select destination airport #############")
        print("### 1. Dublin (DUB)")
        print("### 2. Edinburgh (EDI)")
        print("### 3. Glasgow (GLA")
        print("### 4. London Heathrow (LHR)")
        print("### 5. London Luton (LTN)")
        print("### 6. Manchester (MAN)")
        print(' ')

        choice = input('Enter your number selection here: ')
        
        if choice == depart:
            print("")
            print("")
            print("############### Data entry error ###################")
            print('Destination and departure airports must be different')
            print("")
            print("")           
        else:
            try:
                int(choice)
            except:
                print("Sorry, you did not enter a valid option")
                print('')
                flag = True
            else:    
                print('Choice accepted!')
                print('')
                flag = False

    return choice


def get_number_days():
    '''
       Handles the number of days selected by the user - user enters a choice
       :returns:
           str: The user choice
       '''

    flag = True

    while flag:

        print("########### Please enter the number of previous days of data you wish to see #############")
        choice = input('Enter your number selection here: ')
        print('')
 
        try:
            int(choice)
        except:
            print("Sorry, you did not enter a valid number")
            print('')
            flag = True
        else:    
            print("########### You have chosen to see data for the last {} days #############".format(choice))
            flag = False
        

    return int(choice)


def convert_men_choice(choice):
    '''
       Converts the users input from integer to the accepted airport values
       :returns:
           str: The converted choice
       '''

    if choice == "1":
        conv_choice = "DUB"
        return conv_choice
    elif choice == "2":
        conv_choice =  "EDI"
        return conv_choice
    elif choice == "3":
        conv_choice =  "GLA"
        return conv_choice
    elif choice == "4":
        conv_choice =  "LHR"
        return conv_choice
    elif choice == "5":
        conv_choice =  "LTN"
        return conv_choice
    else:
        conv_choice =  "MAN"
        return conv_choice

def get_data( depart, dest,days):
    '''
       Gets the number of days selected by the user based on the departure and destination airport
       :returns:
           str: The extracted days
       '''
    try:
        df = pd.read_csv('Task4a_data.csv')
    except FileNotFoundError:
        print(' ')
        print('Data file cannot be found')
    extract = df.loc[(df['From'] == depart) & (df['To'] == dest)]
    extract_days = extract.iloc[: , -days: ]
    print("We have found these flights that match your criteria:")
    print(' ')
    return extract_days

def departure_airport_that_has_the_most_passengers_over_time():
    '''
       Gets the departure airport with the most passengers over time
       :returns:
           A dataframe showing the most passengers on each date for the departure airport
           str: The departure airport that has the most passengers over time
       '''

    try:
        df = pd.read_csv('Task4a_data.csv')
    except FileNotFoundError:
        print(' ')
        print('Data file cannot be found')

    date_columns_only = df.iloc[:, 3:]
    departure_airport_and_date_columns = df.groupby('From')[date_columns_only.columns].sum()

    departure_airport_and_date_columns['Total'] = departure_airport_and_date_columns.sum(axis = 1)

    departure_airport_most_passengers_over_time = departure_airport_and_date_columns['Total'].idxmax()
    departure_airport_most_passengers_over_time_values = departure_airport_and_date_columns['Total'].max()

    print(departure_airport_and_date_columns.to_string(index=False))
    print('')
    print(f"The departure airport that has the most passengers over time is {departure_airport_most_passengers_over_time}, with a whooping passengers number of {departure_airport_most_passengers_over_time_values}")


def AM_and_PM_flights_for_two_selected_routes(depart_route_1, destination_route_1, depart_route_2, destination_route_2):
    '''
       Gets the AM and PM for the selected routes
       :returns:
           A dataframe showing the details and time for the two selected routes
       '''
    try:
        df = pd.read_csv('Task4a_data.csv')
    except FileNotFoundError:
        print(' ')
        print('Data file cannot be found')

    selected_routes = df.loc[((df['From'] == depart_route_1) & (df['To'] == destination_route_1)) |  ((df['From'] == depart_route_2) & (df['To'] == destination_route_2))]

    time_selected_routes_AM = selected_routes.loc[selected_routes['Time'] == 'AM']
    time_selected_routes_PM = selected_routes.loc[selected_routes['Time'] == 'PM']
    print(f"The flights of the selected routes for AM are: \n\n{time_selected_routes_AM.to_string(index=False)}")
    print(' ')
    print(f"The flights of the selected routes for PM are: \n\n{time_selected_routes_PM.to_string(index=False)}")
    print(' ')


def run_program():
    '''
       Handles the execution of the entire program
    '''

    main_menu_choice = main_menu()

    if main_menu_choice == '1':
        print('Choice accepted!')
        print('')
        depart_airport = get_depart()

        destination_airport = get_destination(depart_airport)

        dep_choice = convert_men_choice(depart_airport)
        dest_choice = convert_men_choice(destination_airport)

        days = get_number_days()
        print('')
        print("You have selected departure from: {}".format(dep_choice))
        print("You have selected destination as: {}".format(dest_choice))

        extracted_data = get_data(dep_choice, dest_choice, days)
        extract_no_index = extracted_data.to_string(index=False)

        print(extract_no_index)

    elif main_menu_choice == '2':
        print('Choice accepted!')
        print('')
        flag = True

        while flag:
            print("########### Airport Destination and Departure #############")
            print("### 1. Dublin (DUB)")
            print("### 2. Edinburgh (EDI)")
            print("### 3. Glasgow (GLA")
            print("### 4. London Heathrow (LHR)")
            print("### 5. London Luton (LTN)")
            print("### 6. Manchester (MAN)")
            print(' ')

            try:
                depart1 = int(input("Enter the Departure Airport for the First Route: "))
                des1 = int(input("Enter the Destination Airport for the First Route: "))
                depart2 = int(input("Enter the Departure Airport for the Second Route: "))
                des2 = int(input("Enter the Destination Airport for the Second Route: "))

                if 1 < depart1 or  des1 > 6:
                    print('You have Selected an Invalid input, Try Again')
                elif 1 <  depart2 or des2 > 6:
                    print('You have Selected an Invalid input, Try Again')
                elif depart1 == des1 or depart2 == des2:
                    print('Destination and departure airports must be different')
                else:
                    flag = False
                    print('Choice Accepted!\n')
                    AM_and_PM_flights_for_two_selected_routes(convert_men_choice(str(depart1)), convert_men_choice(str(des1)), convert_men_choice(str(depart2)), convert_men_choice(str(des2)))
            except:
                print('Please enter the correct option\n')

    elif main_menu_choice == '3':
        print('Choice accepted!')
        print('')
        departure_airport_that_has_the_most_passengers_over_time()
    else:
        print('Invalid Choice,please try again')

run_program()



