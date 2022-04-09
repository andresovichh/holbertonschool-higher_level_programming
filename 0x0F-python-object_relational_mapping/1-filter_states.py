#!/usr/bin/python3
"""
list all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    """ the guard """
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY\
                   'N%' ORDER BY id ASC")
    result = cursor.fetchall()
    for row in result:
        print(row)
