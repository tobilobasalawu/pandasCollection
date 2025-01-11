import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('dataset.csv')
print(df)

#Filter and Analyze High Performers

print(df.loc[(df['Math'] > 85) & (df['English'] > df['Science'])])

