import sqlite3

import pandas as pd

df = pd.read_csv(
    "C:\\Users\\Welcome\\.cache\\kagglehub\\datasets\\rabieelkharoua\\students-performance-dataset\\versions\\2\\Student_performance_data _.csv")
df.columns = df.columns.str.strip()
connection = sqlite3.connect("F:\\All_Projs\\Python_Proj\\code_practise\\ds_charts\\projcet_01\\school.db")
cursor = connection.cursor()
df.to_sql("student_data", connection, if_exists="replace")

connection.close()
