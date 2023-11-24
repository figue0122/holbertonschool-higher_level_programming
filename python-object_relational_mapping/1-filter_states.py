#!/usr/bin/python3

# Import necessary modules
import MySQLdb
import sys

# Check if the script is being run as the main program
if __name__ == "__main__":
    # Establish a connection to the MySQL database
    cnx = MySQLdb.connect(
        host="localhost",
        port=3306,
        charset="utf8",
        user=sys.argv[1],
        passwd=sys.argv[2],
        database=sys.argv[3])

    # Create a cursor object for executing SQL queries
    cur = cnx.cursor()

    # Execute a SELECT query to retrieve states with names starting with 'N'
    cur.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")

    # Fetch all rows from the executed query
    query_rows = cur.fetchall()

    # Iterate through the query results and print states starting with 'N'
    for row in query_rows:
        if row[1][0] == 'N':
            print(row)

    # Close the cursor to free up resources
    cur.close()

    # Close the connection to the database
    cnx.close()
