import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('dataset.csv')
print(df)

'''
#Filter and Analyze High Performers

#print(df.loc[(df['Math'] > 85) & (df['English'] > df['Science'])])

'''
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
