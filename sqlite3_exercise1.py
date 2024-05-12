import sqlite3

# Connect to the database
connection = sqlite3.connect("music_artists.db")
cursor = connection.cursor()

# Drop the Music_Artists table if it exists
cursor.execute("DROP TABLE IF EXISTS Music_Artists")

# Create "Music_Artists" table
try:
    cursor.execute("""CREATE TABLE Music_Artists (artist TEXT, genre TEXT, number_recordings INTEGER)""")
    connection.commit()
except:
    pass

# Drop the Genre table if it exists
cursor.execute("DROP TABLE IF EXISTS Genre")

# Create "Genre" table
try:
    cursor.execute("""CREATE TABLE Genre (genre TEXT, city TEXT)""")
    connection.commit()
except:
    pass

# Drop the Cities table if it exists
cursor.execute("DROP TABLE IF EXISTS Cities")

# Create "Cities" table with "city" (Primary Key), "state", "zip code", and "population" columns
try:
    cursor.execute("""CREATE TABLE Cities (city TEXT PRIMARY KEY, state TEXT, zip_code TEXT, population INTEGER)""")
    connection.commit()
except:
    pass

# Data to be inserted into "Music_Artists" table
# artist, genre, number_recordings
Music_Artists = [
    ("Miley", "Rock", 14),
    ("Dolly", "Country", 123),
    ("Eminem", "HipHop", 98),
    ("Brittany", "Rock", 37)
]

# Data to be inserted into "Genre" table
# genre, city
Genre = [
    ("Rock", "Los Angeles"),
    ("Hippie", "Eugene"),
    ("Opera", "Florence")
]

# Data to be inserted into "Cities" table
# city, state, zip_code, population
Cities = [
    ("Los Angeles", "CA", "66666", 10000000),
    ("Eugene", "OR", "55555", 800000),
    ("Nashville", "TN", "11111", 1500000),
]

# Insert data into the Music_Artists table
cursor.executemany("INSERT INTO Music_Artists VALUES (?, ?, ?)", Music_Artists)

# Insert data into the Genre table
cursor.executemany("INSERT INTO Genre VALUES (?, ?)", Genre)

# Insert data into the Cities table
cursor.executemany("INSERT INTO Cities VALUES (?, ?, ?, ?)", Cities)

# Join the Music_Artists and Genre tables
cursor.execute("SELECT * FROM Music_Artists INNER JOIN Genre ON Music_Artists.genre = Genre.genre")

# Join the Genre and Cities tables
cursor.execute("SELECT * FROM Genre INNER JOIN Cities ON Genre.city = Cities.city")

# print Music_Artists rows
for row in cursor.execute("SELECT * FROM Music_Artists"):
    print(row)

# Spacing for readability
print()

# Print Genre rows
for row in cursor.execute("SELECT * FROM Genre"):
    print(row)

# Spacing for readability
print()

# From Music_Artists table, select rows where genre matches genre in "Genre" table
for row in cursor.execute("SELECT * FROM Music_Artists WHERE genre IN (SELECT genre FROM Genre)"):
    # Print the artist
    print(row[0])

# Spacing for readability
print()

# Create a query asking the user which artist they want to know more about
artist = input("Enter an artist to learn more about: ")
# Query the database for the artist
cursor.execute("""
    SELECT Music_Artists.genre, Music_Artists.artist, Music_Artists.number_recordings, Genre.city, Cities.population
    FROM Music_Artists
    LEFT JOIN Genre ON Music_Artists.genre = Genre.genre
    LEFT JOIN Cities ON Genre.city = Cities.city
    WHERE Music_Artists.artist=?
""", (artist,))

# Fetch the result
result = cursor.fetchone()

# Print the response
if result:
    if result[3] is None:  # If the artist's genre is not in the Genre table
        print(f"{result[0]} artist {result[1]} has {result[2]} recordings and is popular everywhere.")
    else:
        print(f"{result[0]} artist {result[1]} has {result[2]} recordings and is most popular in {result[3]} with a population of {result[4]}.")
else:
    print("No data found for the given artist.")

# Close the connection
connection.close()
