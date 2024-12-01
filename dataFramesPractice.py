import pandas as pd #importing pandas module
import numpy as np #importin numpy module


#to create an df using numpy
data = np.array([[1, 4], [2,5], [3,6]])
print(pd.DataFrame(data, index=['row1', 'row2', 'row3'], columns=['col1', 'col2']))

