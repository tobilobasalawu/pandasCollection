import pandas as pd
df = pd.read_csv("student_scores.csv")
print(df)

#all rows where the "Math" column is greater than 85, and only the "Name" and "Math" columns.
row = df[df.loc[:, 'Math'] > 85]
print(row.loc[:, ['Name', 'Math']])

'''

'''