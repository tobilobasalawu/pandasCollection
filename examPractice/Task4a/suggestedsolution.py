import pandas as pd  # Importing pandas for data handling
import matplotlib.pyplot as plt  # Importing matplotlib for data visualization


def main_menu():
    """Displays the main menu and gets user selection."""
    while True:
        print("""
        #################################################
        #### Welcome to Elanp Air Flight Data System ####
        #################################################

        ########### Please select an option #############
        1. View passenger numbers
        2. View AM and PM flights for two selected routes
        3. Find the departure airport with the most passengers over time
        """)

        choice = input("Enter your selection: ")
        if choice.isdigit() and choice in {'1', '2', '3'}:
            return choice
        print("Invalid input. Please enter a valid option (1, 2, or 3).")


def get_airport_choice(prompt):
    """Prompts the user to select an airport and validates the input."""
    airports = {
        "1": "DUB",
        "2": "EDI",
        "3": "GLA",
        "4": "LHR",
        "5": "LTN",
        "6": "MAN"
    }
    while True:
        print("\n########### Select an Airport ###########")
        for key, value in airports.items():
            print(f"{key}. {value}")

        choice = input(prompt)
        if choice in airports:
            return airports[choice]
        print("Invalid input. Please enter a valid number (1-6).")


def get_number_of_days():
    """Prompts the user to enter the number of days and validates input."""
    while True:
        choice = input("\nEnter the number of previous days of data you wish to see: ")
        if choice.isdigit() and int(choice) > 0:
            return int(choice)
        print("Invalid input. Please enter a positive integer.")


def get_data(depart, dest, days):
    """Retrieves flight data from CSV based on user selection."""
    try:
        df = pd.read_csv('Task4a_data.csv')
    except FileNotFoundError:
        print("\nError: Data file not found. Please ensure 'Task4a_data.csv' is available.")
        return None

    extract = df.loc[(df['From'] == depart) & (df['To'] == dest)]
    if extract.empty:
        print("No flights found for the selected route.")
        return None

    return extract.iloc[:, -days:]  # Return only the last 'days' columns


def get_busiest_departure_airport():
    """Finds the departure airport with the most passengers over time and displays it with a bar chart."""
    try:
        df = pd.read_csv('Task4a_data.csv')
    except FileNotFoundError:
        print("\nError: Data file not found.")
        return

    date_columns_only = df.iloc[:, 3:]
    departures = df.groupby('From')[date_columns_only.columns].sum()
    departures['Total'] = departures.sum(axis=1)
    busiest_airport = departures['Total'].idxmax()
    max_passengers = departures['Total'].max()

    print(departures.to_string(index=False))
    print(f"\nThe busiest departure airport is {busiest_airport} with {max_passengers} passengers.")

    # Plot results
    plt.figure(figsize=(10, 5))
    departures['Total'].plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title('Total Passengers per Departure Airport')
    plt.xlabel('Airport')
    plt.ylabel('Total Passengers')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()


def get_am_pm_flights():
    """Displays AM and PM flights for two selected routes with a bar chart."""
    print("Select first route:")
    dep1, dest1 = get_airport_choice("Enter departure: "), get_airport_choice("Enter destination: ")
    print("Select second route:")
    dep2, dest2 = get_airport_choice("Enter departure: "), get_airport_choice("Enter destination: ")

    try:
        df = pd.read_csv('Task4a_data.csv')
    except FileNotFoundError:
        print("\nError: Data file not found.")
        return

    routes = df.loc[((df['From'] == dep1) & (df['To'] == dest1)) | ((df['From'] == dep2) & (df['To'] == dest2))]
    if routes.empty:
        print("No matching flights found.")
        return

    print("\nAM Flights:")
    am_flights = routes[routes['Time'] == 'AM']
    print(am_flights.to_string(index=False))

    print("\nPM Flights:")
    pm_flights = routes[routes['Time'] == 'PM']
    print(pm_flights.to_string(index=False))

    # Plot results
    plt.figure(figsize=(8, 5))
    counts = [len(am_flights), len(pm_flights)]
    labels = ['AM Flights', 'PM Flights']
    plt.bar(labels, counts, color=['blue', 'orange'], edgecolor='black')
    plt.title('Number of AM and PM Flights')
    plt.ylabel('Number of Flights')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()


def run_program():
    """Main function to execute the program."""
    while True:
        choice = main_menu()
        if choice == '1':
            depart = get_airport_choice("Enter departure airport: ")
            dest = get_airport_choice("Enter destination airport: ")
            days = get_number_of_days()
            data = get_data(depart, dest, days)
            if data is not None:
                print(data.to_string(index=False))
        elif choice == '2':
            get_am_pm_flights()
        elif choice == '3':
            get_busiest_departure_airport()

        retry = input("\nWould you like to perform another search? (y/n): ").lower()
        if retry != 'y':
            print("Exiting the system. Goodbye!")
            break


# Run the program
run_program()
