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
    cur.execute("SELECT cities.state_id, cities.name, states.id\
                FROM cities JOIN states WHERE cities.state_id = states.id")
    cities = cur.fetchall()

    for city in cities:
        print(city)
