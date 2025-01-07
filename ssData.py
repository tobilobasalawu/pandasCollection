import pandas as pd

#CSV file
df = pd.read_csv('student_scores.csv')
print(df)

#Complex Iloc operations

'''
#Select all rows where the value in column 2 is greater than 50.
ans = df[df.iloc[:,2] > 80]
print(ans['Science'])

#Select the last 3 rows and the last 2 columns.
print(df.iloc[-3:,-2:])

'''

#Select rows 1 to 5 and columns 0, 3, and 4.
print(df.iloc[:5, [0,1,3]])














'''
#Extract the value of Science marks for Diana using iloc
#print(df.iloc[3,2])

#Retrieve the Math and Science columns for the first four rows using iloc
#print(df.iloc[:4,[1,2]])

#Find the sum of all English marks using iloc
#print(df.iloc[:, 3].sum())

#Replace the Science score of Charlie with 80 using iloc.
#ans = df.iloc[2,2] = 80
#print(df)

#Find the mean of the Math scores for the first three students using iloc.
#print(df.iloc[:3, 1].mean())

#Extract the rows for Alice and Bob and print only their English scores using
#print(df.iloc[:2, 3])

#ans = 
#print(ans)
#df['Total'] = df.iloc[:,[1,2,3]].sum(axis=1)
#print(df)
'''