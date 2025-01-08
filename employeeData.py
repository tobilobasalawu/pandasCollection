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