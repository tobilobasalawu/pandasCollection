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



departure_airport_that_has_the_most_passengers_over_time()