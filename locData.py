import pandas as pd
df = pd.read_csv("student_scores.csv")
print(df)

print(df.loc[df.loc[:, 'Math'] == df.loc[:, 'English'], 'Name'])

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

#Replace the "Math" value for "Diana" with the sum of her "Science" and "English" scores.
df.loc[3, 'Math'] = df.loc[3, ['Science', 'English']].sum()
print(df)

#Finding the average scores of science colum
print(df.loc[:, 'Science'].mean())

#a subset of the DataFrame where the "English" column has values greater than or equal to 85, and update their "Math" scores to 100
ans = df.loc[df.loc[:, 'English'] >= 85]
ans.loc[:,'Math'] = 100
print(ans)

#sorting values in descending order
df.sort_values(by='Science',inplace=True, ascending=False)
print(df.loc[:2, 'Science'])
'''