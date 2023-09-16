#!/usr/bin/python3
"""
a script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cnt = cur.execute("SELECT cities.name FROM cities \
                      WHERE state_id = \
                      (SELECT id FROM states WHERE name LIKE BINARY %s) \
                      ORDER BY cities.id", (argv[4],))
    rows = cur.fetchall()

    i = 1
    for row in rows:
        if i != cnt:
            print(row[0], end=', ')
        else:
            print(row[0])
        i += 1
    cur.close()
    db.close()
