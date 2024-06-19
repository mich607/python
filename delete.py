import sqlite3

conn = sqlite3.connect('test.db')
print("successfully connected")

conn.execute(" DELETE FROM TEACHERS WHERE ID=2")
conn.commit()

data = conn . execute("select * FROM TEACHERS")
for teachers in data:
    print("ID :", teachers[0])
    print("firstname :", teachers[1])
    print("lastname:", teachers[2])
    print("age:", teachers[3])
    print("salary:", teachers[4])

print("successfully")
conn.close()