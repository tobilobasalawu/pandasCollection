import pandas as pd

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


the_types_of_post_that_get_the_most_interactions()