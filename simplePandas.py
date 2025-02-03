import pandas as pd

df = pd.read_csv('kidsData.csv')
print(df)

def firstFiveRows():
  print(df.iloc[:5])