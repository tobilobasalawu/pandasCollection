import pandas as pd
df = pd.read_csv("student_scores.csv")
print(df)

#updating english column for alice to 95
df.loc[0, 'English'] = 95
print(df)



'''
#all rows where the "Math" column is greater than 85, and only the "Name" and "Math" columns.
row = df[df.loc[:, 'Math'] > 85]
print(row.loc[:, ['Name', 'Math']])
'''