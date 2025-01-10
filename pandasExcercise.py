import pandas as pd
df = pd.read_csv('student_scores.csv')

print(df)

'''
#Row and Column Selection 
print(df.iloc[1:4, 1:3].sum())

print(df.loc[df['Math'] > 85, ['Name', 'Math']])

#Row Selection with Conditions
print(df.iloc[-2:, 2].mean())

print(df.loc[df['English'] > df['Science'], ['Name', 'English', 'Science']])

'''

#Column Operations
df['Math'] = df.iloc[:, 1] * 2
print(df)

df['Average_score'] = df.loc[:, ['Math', 'Science', 'English']].mean(axis=1)
print(df)