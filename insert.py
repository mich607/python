
import sqlite3

conn = sqlite3.connect('text .db')
print("success")

conn.execute("INSERT INTO TEACHERS VALUE(1,'JONTE','OLOO',24,56000.00)")
conn.execute("INSERT INTO TEACHERS VALUE(2,'MUSA','MUSA',44,25000.00)")
conn.execute("INSERT INTO TEACHERS VALUE(3,'AKARANGA','JADOUNG',34,23000.00)")
conn.execute("INSERT INTO TEACHERS VALUE(4,'SIRJAYO','MOSA',44,90000.00)")
conn.execute("INSERT INTO TEACHERS VALUE(5,'CHOMBA','HOMO',54,60000.00)")

conn.commit()
print("success")