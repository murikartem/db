import sqlite3


con = sqlite3.connect('data3.db')

cursor = con.cursor()


a = str(input('what form you want'))
print(a)
if a == 'капсулы':
   cursor.execute("SELECT * FROM medicines WHERE form='капсулы'")
elif a == 'сироп':
   cursor.execute("SELECT * FROM medicines WHERE form='сироп'")
elif a == 'таблетки':
   cursor.execute("SELECT * FROM medicines WHERE form='таблетки'")
elif a == 'капли':
   cursor.execute("SELECT * FROM medicines WHERE form='капли'")
elif a == 'ампулы':
   cursor.execute("SELECT * FROM medicines WHERE form='ампулы'")
print(cursor.fetchall())
