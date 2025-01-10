import pandas as pd
df = pd.read_csv('student_scores.csv')

print(df)

'''
#Row and Column Selection 
print(df.iloc[1:4, 1:3].sum())

print(df.loc[df['Math'] > 85, ['Name', 'Math']])
'''
