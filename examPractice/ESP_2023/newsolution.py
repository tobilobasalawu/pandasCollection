import pandas as pd
import matplotlib.pyplot as plt
from numpy.f2py.crackfortran import kindselector


def the_types_of_post_that_get_the_most_interactions():
    df = pd.read_csv("Task4a_data.csv")

    interaction_filter_by_post = df.groupby('Post Type').agg({
        'Likes' : 'sum',
        'Shares' : 'sum',
        'Comments' : 'sum'
    })

    interaction_filter_by_post['Total'] = interaction_filter_by_post.sum(axis=1)
    type_of_post_with_most_interaction = interaction_filter_by_post['Total'].idxmax()
    most_interaction_value = max(interaction_filter_by_post['Total'])
    print(f'\nThe type of post with the most interactions is {type_of_post_with_most_interaction}\nWith a total of {most_interaction_value} interactions')

    the_types_of_post_that_get_the_most_interactions_chart(interaction_filter_by_post)

    return interaction_filter_by_post

def the_types_of_post_that_get_the_most_interactions_chart(data):
    data = data.reset_index()
    plt.bar(data.iloc[:, 0], data.loc[:, 'Total'], color='skyblue')

    plt.title('The Post Type with the most interactions')
    plt.ylabel('Post Type')
    plt.xlabel('Total Interactions')
    plt.show()


def how_different_types_of_post_perform_at_different_times_of_the_day():
    df = pd.read_csv("Task4a_data.csv")

    post_choice = input('\nEnter the Post Type you would like to check: ').capitalize()
    time_choice = input('Enter the time of the day you would like to check: ')

    post_type_time = df.loc[(df['Post Type'] == post_choice) & (df['Time'] == time_choice)]
    print(f"\nHow {post_choice} performs between {time_choice}:\n\n{post_type_time.to_string(index=False)}")

    how_different_types_of_post_perform_at_different_times_of_the_day_chart(df, post_choice)

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


how_different_types_of_post_perform_at_different_times_of_the_day()