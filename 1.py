import sqlite3


con = sqlite3.connect('data.db')

cursor = con.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS name_table
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                rate INTEGER DEFAULT 0,
                year INTEGER DEFAULT 0,
                creator TEXT,
                genre TEXT)
''')

#cursor.execute("INSERT INTO name_table(name, rate, year, creator, genre) VALUES ('escape from Soushek', 9.3, 1994, 'Frank Darabont', 'drama'), ('12 angry mans', 9.0, 1957, 'Sindi Lumet', 'drama'), ('Owner of rings:King Returns', 9.0, 2003, 'Piter Jackson', 'fantasy')")
#con.commit()
cursor.execute("SELECT * FROM name_table WHERE genre='drama'")
print(cursor.fetchall())