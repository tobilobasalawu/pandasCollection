import pandas as pd

df = pd.read_csv("favourite_animals.csv")

'''
print(df.dtypes) #To display the data types of each columns

print(df['Apples'].mean()) #Average number of apples consumed

print(max(df['Oranges'])) #Max number of oranges consumed

print(df['Bananas'].sum()) #Displaying the total number of bananas consumed

df['Total_Fruits'] = df[['Apples', 'Oranges', 'Bananas']].sum(axis=1)
print(df)

print(df['Total_Fruits'].mean()) #average of Total_Fruits Column

df.to_csv('Fruits_totals.csv')
'''

print(df)




