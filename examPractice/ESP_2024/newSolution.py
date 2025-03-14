import pandas as pd

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

income_on_different_days_of_the_week()
print(' ')
different_payment_types_and_income_sources()
