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

#Column Operations
df['Math'] = df.iloc[:, 1] * 2
print(df)

df['Average_score'] = df.loc[:, ['Math', 'Science', 'English']].mean(axis=1)
print(df)

#Combining loc and iloc
newDf = df.iloc[2:5]
print(newDf.loc[:,'Math'] > 80)

oldDf = df.loc[df['Math'] > 85]
print(oldDf.iloc[:, -2:])

#Advanced Filtering
df['TotalScore'] = df[['Math', 'Science', 'English']].sum(axis=1)
print(df.loc[df['TotalScore'] > 250])

ans = df.iloc[::-1]
ans.sort_values(by='Name',ascending=False, inplace=True)
print(ans)
'''

#Mixed Indexing 
ans = df.loc[df['Science'] > 80]
#print(ans.iloc[:3])

ss = df.iloc[1:5:2]
print(ss.loc[:, ['Name', 'Math']])
