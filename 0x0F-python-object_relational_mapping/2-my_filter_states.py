#!/usr/bin/python3
"""
Module 2-my_filter_states
Takes in an argument and displays the sates table
  where name matches the arguemt
"""
from sys import argv
import MySQLdb

if (__name__ == '__main__'):
    conn = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("SELECT id, name  FROM states WHERE name LIKE BINARY '{}'"
                .format(argv[4]))
    query = cur.fetchall()
    for row in query:
        print(row)
    cur.close()
    conn.close()
