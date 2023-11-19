#!/usr/bin/python3

"""
Query that is protected against SQL injection to get data from DB
"""

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities JOIN states ON\
                cities.state_id = states.id WHERE states.name = (%s)", (sys.argv[4],))
    states = cur.fetchall()

    for state in states:
        if state is not states[len(states) - 1]:
            print(state[0], end=", ")
        else:
            print(state[0])
