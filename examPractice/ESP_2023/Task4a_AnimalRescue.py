import pandas as pd
import matplotlib.pyplot as plt



def main_menu():
    flag = True

    while flag:

        print("#################################################")
        print("############## Snowy Animal Rescue ##############\n#################################################\n")
        print("########### Please select an option #############")
        print("### 1. Average Social Media Interaction Data")
        print("### 2. Types of post that get the most interactions")
        print("### 3. How different types of post perform at different times of the day")

        choice = input('\nEnter your number selection here: ')

        try:
            if choice.isdigit() and choice in {'1', '2', '3'}:
                int(choice)
                print('Choice accepted!')
                flag = False
            else:
                print('Invalid Choice Selected, Please select a valid choice from the menu\n')
                flag = True
        except:
            print("Sorry, you did not enter a valid option")
            flag = True

    return choice


def average_menu ():
    flag = True
    average_interaction_menu = {
        '1' : 'Likes',
        '2' : 'Shares',
        '3' : 'Comments'
    }
    while flag:

        print("\n#################################################")
        print("############## Average Interaction ##############\n#################################################\n")
        print("########### Please select an option for the average you would like to view #############")
        for key,value in average_interaction_menu.items():
            print(f"{key}. {value}")

        choice = input('\nEnter your number selection here: ')

        try:
            if choice.isdigit() and choice in {'1', '2', '3'}:
                int(choice)
                print('Choice accepted!')
                flag = False
            else:
                print('Invalid Choice Selected, Please select a valid choice from the menu\n')
                flag = True

        except:
            print("Sorry, you did not enter a valid option")
            flag = True

    return average_interaction_menu[choice]

def get_avg_data(avg_choice):
    
    df = pd.read_csv("Task4a_data.csv")
    extract = df.groupby(['Date'], as_index=False) [avg_choice].mean()
    extract_no_index = extract.to_string(index=False)
    
    print("\nHere is the average number of {} each day during the campaign:".format(avg_choice))
    return extract_no_index

def the_types_of_post_that_get_the_most_interactions():
    try:
        df = pd.read_csv("Task4a_data.csv")
        if df.empty:
            raise ValueError
        df = pd.read_csv("Task4a_data.csv")

        interaction_filter_by_post = df.groupby('Post Type').agg({
            'Likes' : 'sum',
            'Shares' : 'sum',
            'Comments' : 'sum'
        })

        interaction_filter_by_post['Total'] = interaction_filter_by_post.sum(axis=1)
        type_of_post_with_most_interaction = interaction_filter_by_post['Total'].idxmax()
        most_interaction_value = max(interaction_filter_by_post['Total'])
        print(f"\n{interaction_filter_by_post}")
        print(f'\nThe type of post with the most interactions is {type_of_post_with_most_interaction}\nWith a total of {most_interaction_value} interactions')

        the_types_of_post_that_get_the_most_interactions_chart(interaction_filter_by_post)
    except ValueError:
        print('The DataFrame is Empty')
    except FileNotFoundError:
        print('The File cannot be found')

def the_types_of_post_that_get_the_most_interactions_chart(data):
    data = data.reset_index()
    plt.bar(data.iloc[:, 0], data.loc[:, 'Total'], color='skyblue')

    plt.title('The Post Type with the most interactions')
    plt.ylabel('Post Type')
    plt.xlabel('Total Interactions')
    plt.show()

def how_different_types_of_post_perform_at_different_times_of_the_day():
    try:
        df = pd.read_csv("Task4a_data.csv")
        if df.empty:
            raise ValueError
        while True:
            post_choice = input('\nEnter the Post Type you would like to check: ').capitalize()
            time_choice = input('\nEnter the time of the day you would like to check: ')

            if post_choice in {'Poll', 'Image', 'News/update', 'Advertisement'}:
                post_type_time = df.loc[(df['Post Type'] == post_choice) & (df['Time'] == time_choice)]
                print(f"\nHow {post_choice} performs between {time_choice}:\n\n{post_type_time.to_string(index=False)}")

                how_different_types_of_post_perform_at_different_times_of_the_day_chart(df, post_choice)
                break
            else:
                print('The Post Type you entered is Invalid, Try Again')
    except ValueError:
        print('The DataFrame is Empty')
    except FileNotFoundError:
        print('The File cannot be found')

def how_different_types_of_post_perform_at_different_times_of_the_day_chart(df, post_choice):
    one_post_type = df[df["Post Type"] == post_choice]

    number_only_values = one_post_type.iloc[:, 3:]
    time_filter_by_intercations = one_post_type.groupby('Time')[number_only_values.columns].mean().reset_index()

    plt.plot(time_filter_by_intercations['Time'], time_filter_by_intercations['Likes'])
    plt.plot(time_filter_by_intercations['Time'], time_filter_by_intercations['Shares'])
    plt.plot(time_filter_by_intercations['Time'], time_filter_by_intercations['Comments'])
    plt.title(f'How {post_choice} perform at different times of the day ')
    plt.ylabel('Average Interactions')
    plt.xlabel('Time')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.legend(['Likes', 'Shares', 'Comments'])
    plt.show()

def execute_main_menu():
    while True:
        main_menu_choice = main_menu()

        if main_menu_choice == "1":
            avg_men_choice = average_menu()
            print(get_avg_data(avg_men_choice))
        elif main_menu_choice == "2":
            the_types_of_post_that_get_the_most_interactions()
        elif main_menu_choice == "3":
            how_different_types_of_post_perform_at_different_times_of_the_day()
        else:
            print('\nInvalid Choice selected, please try again')

        ask_to_run_again = input("\nWould you like to continue\nIf Yes - 'y'\nIf No - 'n'\n=>").lower()
        if ask_to_run_again != 'y':
            print('\nThank you for the Snowy Animal rescue program')
            break

execute_main_menu()


