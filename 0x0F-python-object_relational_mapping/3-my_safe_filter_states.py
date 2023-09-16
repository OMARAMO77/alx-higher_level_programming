#!/usr/bin/python3
"""
a script that takes in arguments and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
But this time, this script is safe from MySQL injections!
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states \
                 WHERE name=%s \
                 ORDER BY id ASC", (argv[4],))
    rows = cur.fetchall()

    for row in rows:
        print(row)
    cur.close()
    db.close()
