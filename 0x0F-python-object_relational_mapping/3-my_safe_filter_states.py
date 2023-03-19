#!/usr/bin/python3
"""
Module 3-my_safe_filter_states
Filters sates safe of SQL injections
"""
from sys import argv
import MySQLdb
if (__name__ == '__main__'):
    conn = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    command = ("SELECT * FROM  states WHERE name=%s")
    cur.execute(command, (argv[4],))
    query = cur.fetchall()
    for row in query:
        print(row)
    cur.close()
    conn.close()
