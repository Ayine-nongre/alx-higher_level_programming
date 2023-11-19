#!/usr/bin/python

"""
Query that is protected against SQL injection to get data from DB
"""

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    cur = db.cursor()
    cur.execute("SELECT cities.name, states.id, cities.state_id FROM cities\
                JOIN states WHERE state.name = (%s)", (sys.argv[4],))
    states = cur.fetchall()

    print(", ".join([state[1] for state in states]))
