import pandas as pd #importing pandas module
import numpy as np #importin numpy module


#to create an df using numpy
data = np.array([[1, 4], [2,5], [3,6]])
#print(pd.DataFrame(data, index=['row1', 'row2', 'row3'], columns=['col1', 'col2']))

#creating dataframes without numpy
data = [['Tobi', 17], ['Harleen', 18], ['Georgia', 18]]
df = pd.DataFrame(data, columns=['Name', 'Age'])
#print(df)

#creating a DataFrame from a dictionary
states = ['Birmingham', 'London', 'Liverpool', 'Manchester']
population = [981492, 992239, 300492, 922103]

dictStates = {
  'States': states,
  'Population' : population
}

dfPopulation = pd.DataFrame(dictStates)
#print(dfPopulation)

#creating a DataFrame from csv
dfExams = pd.read_csv('StudentsPerformance.csv')

#show first 5 rows in df - default head is 5
#print(dfExams.head())

#how to show the DataFrame
#print(dfExams.head(10))

# to show the last rows(10)
#print(dfExams.tail(10)) 

#to get the number of rows of the dataframe
#print(dfExams.shape)

#to display all the rows
pd.set_option('display.max_rows', 1000)
#print(dfExams)

'''
#Attributes in pandas
print(dfExams.shape) #getting the no if rows and columns

print(dfExams.index) #access the index attribute

print(dfExams.columns) #gettng each column name and its attribute

print(dfExams.dtypes) #to get the data types

print(dfExams.info()) #to get infor about the table

print(dfExams.describe()) #GIVES basic statistics like max, min,count mean...

'''


'''
#Functions
print(len(dfExams)) # no of rows in a dataframe

print(max(dfExams.index)) #returns the maximun index in a df

print(min(dfExams.index)) #returns the minimum index in a df

print(type(dfExams)) #the type of the dataframe

print(round(dfExams, 2)) #round the content 2 dp
'''



#selection one column in dataframe
#print(dfExams['gender'])
#print(type(dfExams['gender']))
#print(dfExams['math score'].head(6)) #getting the first 6 rows of the column math score

#selecting two or more column in a dataframe
result = dfExams[['gender', 'math score', 'reading score', 'writing score']]
print(dfExams.loc[3])