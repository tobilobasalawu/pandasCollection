import pandas as pd

df = pd.read_csv("fruit_consumption.csv")

print(df.dtypes) #To display the data types of each columns

print(df['Apples'].mean()) #Average number of apples consumed

print(max(df['Oranges'])) #Max number of oranges consumed

print(df['Bananas'].sum()) #Displaying the total number of bananas consumed

df['Total_Fruits'] = df[['Apples', 'Oranges', 'Bananas']].sum(axis=1)
print(df)

print(df['Total_Fruits'].mean()) #average of Total_Fruits Column