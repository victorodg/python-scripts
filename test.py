# read './Files/file.xlsx' into dataframe 'df'. Where sheet name is 'Sheet1'

import pyodbc
import pandas as pd

df = pd.read_excel('./Files/file.xlsx', sheet_name='Sheet1')

# print(df)

# Upload df to SQL Server

conn = pyodbc.connect(
    'Driver={SQL Server};Server=DESKTOP-1000;Database=test;Uid=sa;Pwd=123456')

df.to_sql('test', conn, if_exists='replace')
