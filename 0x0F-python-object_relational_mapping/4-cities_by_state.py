#!/usr/bin/python3
"""
Module 4-cities_by_state
list all cites from db via inner join
"""
import MySQLdb
from sys import argv
if __name__ == '__main__':
    conn = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name from states " +
                "JOIN cities ON states.id = cities.state_id;")
    query = cur.fetchall()
    for row in query:
        print(row)
    cur.close()
    conn.close()
