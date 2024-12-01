import pandas as pd #importing pandas module
import numpy as np #importin numpy module


#to create an df using numpy
data = np.array([[1, 4], [2,5], [3,6]])
#print(pd.DataFrame(data, index=['row1', 'row2', 'row3'], columns=['col1', 'col2']))

#creating dataframes without numpy
data = [['Tobi', 17], ['Harleen', 18], ['Georgia', 18]]
df = pd.DataFrame(data, columns=['Name', 'Age'], index=['row1', 'row2', 'row3'])
print(df)
