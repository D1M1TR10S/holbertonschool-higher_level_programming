#!/usr/bin/python3
"""A script that lists all cities with their ids and states
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("\
                SELECT cities.name \
                FROM cities \
                INNER JOIN states \
                ON cities.state_id = states.id \
                WHERE states.name = %s", (argv[4],))
    query = cur.fetchall()
    city_list = [i[0] for i in query]
    print(', '.join(city_list))
    cur.close()
    db.close()
