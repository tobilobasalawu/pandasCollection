import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('dataset.csv')
print(df)

'''
#Filter and Analyze High Performers

print(df.loc[(df['Math'] > 85) & (df['English'] > df['Science'])])

#Aggregate Scores by Subject

average = df[['Math', 'Science', 'English']].mean()
total = df[['Math', 'Science', 'English']].sum()
newdf = pd.DataFrame({'Average' : average, 'Total' : total})
newdf.to_csv('subject_aggregates.csv', index=False)

#Custom Visualization
plt.bar(['Math', 'Science', 'English'], newdf['Average'])
plt.title('Custom Visualization')
plt.xlabel('Subjects')
plt.ylabel('Total Scores')

plt.show()

#Top Performers Visualization
df['Total'] = df[['Math', 'Science', 'English']].sum(axis=1)
print(df.loc[df['Total'] > 250])

df.to_csv('top_performers.csv')

plt.pie(df['Total'], labels=df['Name'], autopct="%1.1f%%")
plt.show()

#5 Trend Analysis of Science Scores
df.sort_values(by='Science', ascending=False, inplace=True)

plt.plot(df['Name'], df['Science'], marker="o")
plt.grid()
plt.xlabel('Name')
plt.show()
'''

print(df.loc[:2, ['Math', 'English']])

df.iloc[4, 2] = 95
print(df)