import pandas as pd
import sys
import matplotlib.pyplot as plt


#The menu() function generates the UI the accepts and validates user choice
def menu():

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
        print("7. Trends and patterns over time") #Added an option to view trends and pattern
        print("######################################################")

        
        menu_choice = input("Please enter the number of your choice (1-7): ")

        try:
            int(menu_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(menu_choice) < 1 or int(menu_choice) > 7:
                print("Sorry, you did not enter a valid choice")
                flag = True
            elif int(menu_choice) == 7:
                trends_menu()
            else:
                return menu_choice  


#Gets the short version of the conversion information based on user menu choice
def get_currency ():
    currencies = {
       '1': 'GBP - EUR',
       '2': 'EUR - GBP', 
       '3': 'GBP - AUD',
       '4': 'AUD - GBP',
       '5': 'GPB - JPY',
       '6': 'JPY - GBP',
       }
   
    currency = currencies.get(menu_choice)
    
    return currency


def trends_menu():
    
    flag = True

    while flag:
        print("######################################################")
        print("Which trends and patterns over time do you want to view today?")
        print("1. Pound (GBP) to US dollar (USD)")
        print("2. US Dollar (USD) to pound (GBP)")
        print("")
        print("######################################################")

        
        menu_choice = input("Please enter the number of your choice (1-2): ")

        try:
            int(menu_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(menu_choice) < 1 or int(menu_choice) > 2:
                print("Sorry, you did not enter a valid choice")
                flag = True
            elif int(menu_choice) == 1:
                trends_GBP_to_USD()
            elif int(menu_choice) == 2:
                pass
            else:
                return menu_choice 

def trends_GBP_to_USD():
    df = pd.read_csv("Task4a_data.csv")

    print("######################################################")
    print("")
    print('Trends/patterns over time for GBP to USD')
    seven_avg = df.iloc[-7:]
    plt.figure(figsize=(12,9))
    print(seven_avg.loc[:, ['Date', 'GBP - USD']])

    plt.plot(round(seven_avg['Date'], 2), seven_avg['GBP - USD'])
    plt.title("TRENDS OVER THE LAST 7 DAYS - 'GBP - USD'")
    plt.xlabel("Date")
    plt.ylabel("GBP - USD")
    plt.grid()
    plt.show()

    #sys.exit(0)

def trends_USD_to_GBP():
    df = pd.read_csv("Task4a_data.csv")

    print("######################################################")
    print("")
    print('Trends/patterns over time for USD TO GBP')
    seven_avg = df.iloc[-7:]
    plt.figure(figsize=(12,9))
    print(seven_avg.loc[:, ['Date', 'USD - GBP']])

    plt.plot(round(seven_avg['Date'], 2), seven_avg['USD - GBP'])
    plt.title("TRENDS OVER THE LAST 7 DAYS - 'USD -GBP'")
    plt.xlabel("Date")
    plt.ylabel("USD - GBP")
    plt.grid()
    plt.show()


menu_choice = menu()
currency = get_currency()



#The get_conversion_rate function uses pandas to get the latest conversion rate
#Imports a csv file in to a data frame
#Uses 'iloc' to get the last/most recent value in the selected column
def get_conversion_rate():
    df = pd.read_csv("Task4a_data.csv")
    
    conversion_rate = round(df[currency].iloc[-1],2)


    return conversion_rate

conversion_rate = get_conversion_rate()


#Accepts and validates user input for the amount they want to convert
def get_amount_to_convert():
    print("You are converting: ",currency)
    
    flag = True
    
    while flag:
        conversion_amount = input("please enter the amount you wish to convert: ")
    
        try:
            float(conversion_amount)
        except:
            print("Sorry, you must enter a numerical value")
            flag = True
        else:
            return conversion_amount  

conversion_amount = float(get_amount_to_convert())

#Performs the converison and outputs the final values
def perfom_conversion():
    amount_recieved = round(conversion_amount * conversion_rate, 2)

    print("##################################")
    print('You are converting {} in {}'.format(conversion_amount, currency[0:3]) )
    print('You will recieve {} in {}'.format(amount_recieved, currency[6:9]))
    
perfom_conversion()
