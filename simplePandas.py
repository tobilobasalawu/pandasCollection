import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('kidsData.csv')
print(df)

def menu():
  try:
    userInput = int(input('\n1. First 5 rows \n2. Science Score greater than 80 \n3. View Bar Chart \nPlease Enter an option: '))
    if userInput == 1:
      firstFiveRows()
    elif userInput == 2:
      scienceHigh()
    elif userInput == 3:
      mathChart()
    else:
      print('Select the correct option')
    
  except:
    print('Select the correct option')
      

def firstFiveRows():
  print(df.iloc[:5])

def scienceHigh():
  print(df.loc[df['Science'] > 80])

def mathChart():
  plt.bar(df['Name'], df['Math'], color='blue')
  plt.xlabel('Names')
  plt.ylabel('Scores')
  plt.title('Student Math Scores')
  plt.show()

menu()
