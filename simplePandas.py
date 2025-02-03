import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('kidsData.csv')
print(df)

def firstFiveRows():
  print(df.iloc[:5])

def scienceHigh():
  print(df.loc[df['Science'] > 80])

def mathChart():
  plt.bar(df[''])