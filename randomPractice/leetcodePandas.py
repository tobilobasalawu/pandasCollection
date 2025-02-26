#ignore all errors thats leetcode IDE doing rubbish, lol

import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
  result = pd.DataFrame(student_data, columns = ['student_id', 'age'])
  return result


#displaying first 3 rows of the DataFrame
import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    result = employees.head(3)
    return result

#displaying the sixe of the dataframe in a list
import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return list(players.shape)