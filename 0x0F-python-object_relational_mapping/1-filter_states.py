#!/usr/bin/python3
"""
Module 1-filter_states
list states with a name starting with N from db
"""
import MySQLdb
from sys import argv

if (__name__ == '__main__'):
    conn = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'" +
                "ORDER BY id ASC")
    query = cur.fetchall()
    for row in query:
        print(row)
    cur.close()
    conn.close()
