#!/usr/bin/python3
"""Fetch all cities from the db
User supplies username, password, and database name as args
Only one execute() call allowed
Cities are sorted in ascending order by id
"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Establish a db connection
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         host='localhost',
                         port=3306)
    cur = db.cursor()

    # Execute a SQL query to fetch all cities
    cmd = """SELECT cities.id, cities.name, states.name
         FROM states
         INNER JOIN cities ON states.id = cities.state_id
         ORDER BY cities.id ASC"""
    cur.execute(cmd)
    allCities = cur.fetchall()

    # Print the fetched cities
    for city in allCities:
        print(city)

    # Close the db connection
    cur.close()
    db.close()
