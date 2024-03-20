import sqlite3

# Connect to the SQLite database file
conn = sqlite3.connect('db.sqlite3')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Execute a SQL query
cursor.execute('SELECT * FROM Product')

# Fetch the results
results = cursor.fetchall()

# Print the results
for row in results:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()
