import sqlite3


conn = sqlite3.connect('test.db')
print("successfully connected to database")

conn.execute("""
CREATE TABLE TEACHERS(
ID INT PRIMARY KEY NOT NULL,
FIRSTNAME TEXT NOT NULL,
LASTNAME TEXT NOT NULL,
AGE INT NOT NULL,
SALARY REAL 

)
""")
print("successfully created table teachers ")
conn.close()