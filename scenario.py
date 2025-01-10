import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('dataset.csv')

print(df)

'''
#Top performers
print(df.loc[(df['Science'] > 85) & (df['Math'] > 85)])

#Average Performer 
df.loc[len(df)] = df[['Math', 'Science', 'English']].mean()
df.iloc[5, 0] = 'Average'
print(df)
'''

#Improvement Opportunity
print(df.loc[df['English'] < df['Math'], ['Name', 'Math', 'English']])