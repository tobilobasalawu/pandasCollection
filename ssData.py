import pandas as pd

#CSV file
df = pd.read_csv('student_scores.csv')
print(df)

#Extract the value of Science marks for Diana using iloc
#print(df.iloc[3,2])

#Retrieve the Math and Science columns for the first four rows using iloc
#print(df.iloc[:4,[1,2]])

#Find the sum of all English marks using iloc
#print(df.iloc[:, 3].sum())

#Retrieve the last two rows of the DataFrame using iloc.
print(df.iloc[-2:])
