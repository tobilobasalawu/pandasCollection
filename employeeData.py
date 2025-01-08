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

#Advanced Selection with loc

#11.	Use .loc to display employees with more than 6 years of experience
#print(df.loc[df.loc[:, 'Experience'] > 6])

#12.	Add a new column, Bonus, where the value is 5% of the Salary. Use .loc to calculate and assign the values.
#df['Bonus'] = df.loc[:, 'Salary'] * 5/100
#print(df)

#13.	Use .loc to display only employees who are older than 30 and earn more than 55,000.
#ans = df.loc[df.loc[:, 'Age'] > 30]
#ans.loc[:, 'Salary'] > 55000
#print(ans)

#14. 14.	Use .loc to modify Charlie's Salary to 60,000.
#df.loc[2, 'Salary'] = 60000
#print(df)

#15.	Use .loc to add a new row for an employee named "Frank" in the Finance department with a Salary of 57,000, Experience of 4 years, and an Age of 29.
#df.loc[len(df)] = ['Frank', 'Finance', 57000, 4, 29]
#print(df)

#Advanced Selection using iloc
#16.	Use .iloc to display the last two rows of the DataFrame.
#print(df.iloc[-2:])

#17. 17.	Use .iloc to modify the Salary in the second row (Bob) to 65,000.
