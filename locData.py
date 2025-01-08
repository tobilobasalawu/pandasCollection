import pandas as pd
df = pd.read_csv("student_scores.csv")
print(df)

#Replace the "Math" value for "Diana" with the sum of her "Science" and "English" scores.
df.loc[3, 'Math'] = df.loc[3, ['Science', 'English']].sum()
print(df)
'''
#all rows where the "Math" column is greater than 85, and only the "Name" and "Math" columns.
row = df[df.loc[:, 'Math'] > 85]
print(row.loc[:, ['Name', 'Math']])

#updating english column for alice to 95
df.loc[0, 'English'] = 95
print(df)

#Create a new column 'Total' which is the sum of the "Math", "Science", and "English" columns, row-wise.
df['Total'] = df.loc[:, ['Math', 'Science', 'English']].sum(axis=1)
print(df)

#Find all rows where the "Science" column is between 80 and 90 (inclusive), and display only the "Name" and "Science" columns.
ans = (df.loc[:, 'Science'] >= 80) & (df.loc[:, 'Science'] <= 90)
print(df.loc[ans, ['Name', 'Science']])

'''