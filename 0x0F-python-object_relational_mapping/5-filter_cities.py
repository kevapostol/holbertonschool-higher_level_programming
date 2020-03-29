#!/usr/bin/python3
"""
A script that takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa
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
    cur.execute("""SELECT cities.name FROM cities, states WHERE \
                cities.state_id = states.id AND states.name \
                = %s""", (argv[4],))

    rows = cur.fetchall()
    print(', '.join(city[0] for city in rows))

    # Close all cursors
    cur.close()
    # Close all databases
    db.close()
