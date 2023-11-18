#!/usr/bin/python3

"""
Query to filter states in ORM
"""

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], host=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE CONVERT(`name` USING Latin1)\
                COLLATE Latin1_General_CS LIKE 'N%';")
    states = cur.fetchall()

    for state in states:
        print(state)
