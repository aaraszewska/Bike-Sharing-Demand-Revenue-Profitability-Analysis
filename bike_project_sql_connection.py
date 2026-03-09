import pandas as pd
import pyodbc

conn = pyodbc.connect(
    r"DRIVER={ODBC Driver 18 for SQL Server};"
    r"SERVER=DESKTOP-AQJSJK9\SQLEXPRESS;"
    r"DATABASE=bike_data;"
    r"Trusted_Connection=yes;"
    r"Encrypt=no;"
    r"TrustServerCertificate=yes;"
)

df = pd.read_sql_query("SELECT * FROM vw_bike_analysis", conn)

print(df.head())
print(df.info())

conn.close()