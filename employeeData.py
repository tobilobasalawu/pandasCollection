import pandas as pd

df = pd.read_csv("employee_salaries.csv")
print(df)

#Basic Selection with Loc

#1Use .loc to display all information about the employee named "Charlie."
#print(df.loc[2])

#2.Use .loc to show the Department and Salary for "Diana."
#print(df.loc[3, ['Salary', 'Department']])

#3Select and display rows for employees in the IT department using .loc.
#print(df.loc[df.loc[:, 'Department'] == 'IT'])

#4.	Use .loc to display the names and salaries of all employees.
#print(df.loc[:, ['Name','Salary']])

#5. 5.	Use .loc to show rows where Salary is greater than 55,000
#print(df.loc[df.loc[:, 'Salary'] > 55000])


#Basic Selection with iloc

#6.	Use .iloc to display the first row of the DataFrame
#print(df.iloc[0])

#7.	Use .iloc to display the third row.
#print(df.iloc[2])

#8. Use .iloc to display the Salary and Experience columns for the first two rows.
#print(df.iloc[:2, [2,3]])

#9.	Use .iloc to display all rows but only the Age column.
#print(df.iloc[:, -1])

#10.	Select rows 1 to 3 (inclusive of 1, exclusive of 4) and columns 2 to 4 (exclusive of column 4) using .iloc.
#print(df.iloc[1:4, 2:4])