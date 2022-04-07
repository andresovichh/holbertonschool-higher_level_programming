#!/usr/bin/python3
"""
Module that lists all states from the database hbtn_0e_0_usa 
"""
import MySQLdb
import sys

""" should be guarded"""
if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port="3306", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM {} ORDER BY ASC".format(sys.argv[3]))
