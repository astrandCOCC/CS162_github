import sqlite3

connection = sqlite3.connect("music_artists.db")
cursor = connection.cursor()

try:
    cursor.execute("""CREATE TABLE Music_Artists (artist TEXT, genre TEXT, number_recordings INTEGER)""")
    connection.commit()
except:
    pass

# Data to be inserted into the database
Music_Artists = [
    ("Miley", "Rock", 14),
    ("Dolly", "Country", 123),
    ("Eminem", "HipHop", 98),
    ("Brittany", "Rock", 37)
]

# Insert data into the database
cursor.executemany("INSERT INTO Music_Artists VALUES (?, ?, ?)", Music_Artists)

# print database rows
for row in cursor.execute("SELECT * FROM Music_Artists"):
    print(row)

# Spacing for readability
print()

# Only print artists with genre "Rock"
for row in cursor.execute("SELECT * FROM Music_Artists WHERE genre='Rock'"):
    print(row)

connection.close()
