#!/usr/bin/python3
"""Script that lists all cities from the database by given state

Usage:
    python3 5-filter_cities.py <username> <password> <database> <state_name>

"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         host='localhost',
                         port=3306)
    cur = db.cursor()
    cmd = """SELECT cities.name
         FROM states
         INNER JOIN cities ON states.id = cities.state_id
         WHERE states.name=%s
         ORDER BY cities.id ASC"""
    cur.execute(cmd, (sys.argv[4],))
    allCities = cur.fetchall()

    print(", ".join([city[0] for city in allCities]))

    cur.close()
    db.close()
