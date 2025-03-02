import pandas as pd

#CSV file
df = pd.read_csv('student_scores.csv')
print(df)

#Complex Iloc operations

#Select all rows where the value in column 2 is greater than 50.
ans = df.loc[df.iloc[:, 2] > 80]
print(ans)

#Select the last 3 rows and the last 2 columns.
print(df.iloc[-3:,-2:])

#Select rows 1 to 5 and columns 0, 3, and 4.
print(df.iloc[:5, [0,1,3]])

#Update the value in the second row, first column (Name) to be the sum of the values in the second row of "Math", "Science", and "English".
df.iloc[1, 0] = df.iloc[1, [1, 2, 3]].sum()
print(df)

#Create a new column 'Difference' which is the difference between the values in "English" and "Math" columns
df['Difference'] = df.iloc[:, 3] - df.iloc[:, 1]
print(df)

#Select the first 3 rows and reverse the order of columns "Name", "Science", and "Math"
row = df[['Name', 'Science', 'Math']]
print(row.iloc[:3, ::-1])

#Create a subset of the DataFrame with only rows where the value in the "English" column is between 80 and 90.
ans = df[df.iloc[:, 3] < 90]
print(ans.iloc[:, 3])

#Replace all values in the "Math" column with the square of the values in the "Science" column for rows where the value in the "Science" column is less than 90
scienceColumn = df[df.iloc[:,2] < 90]
df.iloc[:3, 1] = scienceColumn.iloc[:3, 2] ** 2
df.iloc[-1, 1] = scienceColumn.iloc[-1, 2] ** 2
print(df)

#Select all the rows where the "Math" column contains a value that is a multiple of 5.
a = df[df.iloc[:, 1] % 5 == 0]
print(a.iloc[:, 1])

#Extract the value of Science marks for Diana using iloc
print(df.iloc[3,2])

#Retrieve the Math and Science columns for the first four rows using iloc
print(df.iloc[:4,[1,2]])

#Find the sum of all English marks using iloc
print(df.iloc[:, 3].sum())

#Replace the Science score of Charlie with 80 using iloc.
ans = df.iloc[2,2] = 80
print(df)

#Find the mean of the Math scores for the first three students using iloc.
print(df.iloc[:3, 1].mean())

#Extract the rows for Alice and Bob and print only their English scores using
print(df.iloc[:2, 3])

#ans = 
print(ans)
df['Total'] = df.iloc[:,[1,2,3]].sum(axis=1)
print(df)
