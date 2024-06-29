#!/usr/bin/python3
"""Fetch all states from a given db

Fetches all states from a MySQL database using the provided username, password
and database name. Orders the states by id in ascending order.

Usage: python3 select_states.py <username> <password> <database>

"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        host='localhost',
        port=3306
    )
    cursor = db.cursor()
    cursor.execute("SELECT id, name FROM states ORDER BY id ASC")
    all_states = cursor.fetchall()

    for state in all_states:
        print(state)

    cursor.close()
    db.close()
