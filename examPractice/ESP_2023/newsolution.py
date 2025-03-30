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


def how_different_types_of_post_perform_at_different_times_of_the_day(post, time):
    df = pd.read_csv("Task4a_data.csv")

    post_type_time = df.loc[(df['Post Type'] == post) & (df['Time'] == time)]
    print(f"\nHow {post} performs between {time}:\n\n{post_type_time.to_string(index=False)}")



the_types_of_post_that_get_the_most_interactions()