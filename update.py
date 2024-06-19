import sqlite3

conn = sqlite3.connect('test.db')
print("successfully connected")

conn.execute("UPDATE TEACHERS SET SALARY=10000.00 WHERE ID =2")
conn.commit()

data = conn.execute("select * FROM TEACHERS")

for teacher in data:
    print("ID :", teacher[0])
    print("firstname :", teacher[1])
    print("lastname:", teacher[2])
    print("age:",teacher[3])
    print("salary:", teacher[4])


