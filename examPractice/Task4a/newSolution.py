from operator import index

import pandas as pd

def departure_airport_that_has_the_most_passengers_over_time():
    df = pd.read_csv('Task4a_data.csv')

    date_columns_only = df.iloc[:, 3:]
    departure_airport_and_date_columns = df.groupby('From')[date_columns_only.columns].sum()

    departure_airport_and_date_columns['Total'] = departure_airport_and_date_columns.sum(axis = 1)

    departure_airport_most_passengers_over_time = departure_airport_and_date_columns['Total'].idxmax()
    departure_airport_most_passengers_over_time_values = departure_airport_and_date_columns['Total'].max()

    print(departure_airport_and_date_columns)
    print(f"The departure airport that has the most passengers over time is {departure_airport_most_passengers_over_time}, with a whooping passengers number of {departure_airport_most_passengers_over_time_values}")


def AM_and_PM_flights_for_two_selected_routes(depart_route_1, destination_route_1, depart_route_2, destination_route_2, time):
    df = pd.read_csv('Task4a_data.csv')

    selected_routes = df.loc[((df['From'] == depart_route_1) & (df['To'] == destination_route_1)) |  ((df['From'] == depart_route_2) & (df['To'] == destination_route_2))]

    time_selected_routes = selected_routes.loc[selected_routes['Time'] == time]
    print(f"The flights for the selected routes are: \n\n{time_selected_routes}")


AM_and_PM_flights_for_two_selected_routes('DUB', 'LHR','DUB', 'MAN', 'AM')