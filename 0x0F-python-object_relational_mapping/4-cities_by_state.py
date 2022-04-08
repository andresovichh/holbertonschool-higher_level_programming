#!/usr/bin/python3
"""
script that takes in an argument and displays
all values in the states table
of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """ the guard """
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cursor = db.cursor()
    cursor.execute("""SELECT cities.id, cities.name, states.name FROM cities\
                   JOIN states ON cities.state_id = states.id ORDER BY\
                   cities.id ASC""")
    result = cursor.fetchall()
    for row in result:
        print(row)
