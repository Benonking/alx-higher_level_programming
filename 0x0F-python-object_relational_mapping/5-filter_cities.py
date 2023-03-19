#!/usr/bin/python3
"""
Module 5-filter_cities
list all cities by state
"""
import MySQLdb
from sys import argv
if __name__ == '__main__':
    conn = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute(""" SELECT cities.name FROM
                cities INNER JOIN states ON states.id = cities.state_id
                WHERE states.name=%s""", (argv[4],))
    query = cur.fetchall()
    list = ()
    for row in query:
        list += row
    print(", ".join(list))
    cur.close()
    conn.close()
