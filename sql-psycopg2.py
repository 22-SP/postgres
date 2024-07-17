import psycopg2

# Connect to chinook database
connection = psycopg2.connect(database="chinook")

# Build a cursor object of the database
cursor = connection.cursor()

# Query 1 - Select all records from the Artist table
cursor.execute('SELECT * FROM "Artist"')

# Fetch the results (multiple)
results = cursor.fetchall()

# Fetchall result (single)
# cursor = results.fetchone()
connection.close()

# Print results
for result in results:
    print(result)