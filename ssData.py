import pandas as pd

#CSV file
df = pd.read_csv('student_scores.csv')
print(df)

#Extract the value of Science marks for Diana using iloc
print(df.iloc[3,2])