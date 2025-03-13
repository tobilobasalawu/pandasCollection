import pandas as pd

def value_of_the_pound_GBP_to_the_US_dollar_USD(days):
    df = pd.read_csv("Task4a_data.csv")
    GBP_US_column = df.iloc[-days:, 7]

    print(f'The values from GBP to USD for the last {days} days is:\n{GBP_US_column.to_string(index=False)}')

def value_of_the_US_dollar_USD_to_the_pound_GBP(days):
    df = pd.read_csv("Task4a_data.csv")
    US_GBP_column = df.iloc[-days:, -1]

    print(f'The values from USD to GBP for the last {days} days is:\n{US_GBP_column.to_string(index=False)}')

value_of_the_pound_GBP_to_the_US_dollar_USD(7)
print(' ')
value_of_the_US_dollar_USD_to_the_pound_GBP(7)