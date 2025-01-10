import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('dataset.csv')

print(df)


#Top performers
print(df.loc[(df['Science'] > 85) & (df['Math'] > 85)])

#Average Performer 
df.loc[len(df)] = df[['Math', 'Science', 'English']].mean()
df.iloc[5, 0] = 'Average'
print(df)

#Improvement Opportunity
print(df.loc[df['English'] < df['Math'], ['Name', 'Math', 'English']])

#Score distribution
print(df.loc[:, ['Math', 'Science', 'English']].sum())

plt.bar(['Math', 'Science', 'English'], df.loc[:, ['Math', 'Science', 'English']].sum())
plt.xlabel('Subjects')
plt.ylabel('Scores')

plt.title('Score Distribution')

plt.savefig('score_distribution.png')

plt.show()


#Trends in Math Scores
df.sort_values(by='Math', ascending=False, inplace=True)

plt.plot(df['Name'], df['Math'], marker = 'o')
plt.xlabel('Names')
plt.ylabel('Scores')
plt.title('Trends in Math Scores')

plt.savefig('top_scorers_pie_chart.png')
plt.show()


df.to_csv('student_performance_report.csv')

