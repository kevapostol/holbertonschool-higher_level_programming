#!/usr/bin/python3
"""
A script that lists all states with a name starting with N (upper N) from the
database hbtn_0e_0_usa

usage: ./<exe> mysql username, mysql password
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    cur.execute("""SELECT * from states WHERE name LIKE BINARY'N%' ORDER BY \
                id ASC""")

    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close all cursors
    cur.close()
    # Close all databases
    db.close()
