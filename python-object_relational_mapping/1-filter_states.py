#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == "__main__":
    cnx = MySQLdb.connect(
        host="localhost",
        port=3306,
        charset="utf8",
        user=sys.argv[1],
        passwd=sys.argv[2],
        database=sys.argv[3])

    cur = cnx.cursor()

    cur.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")

    query_rows = cur.fetchall()

    for row in query_rows:
        if row[1][0] == 'N':
            print(row)

    cur.close()

    cnx.close()
