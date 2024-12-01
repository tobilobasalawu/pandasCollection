import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
  result = pd.DataFrame(student_data, columns = ['student_id', 'age'])
  return result

#ignore list error thats leetcode IDE

#displaying first 3 rows of the DataFrame
import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    result = employees.head(3)
    return result