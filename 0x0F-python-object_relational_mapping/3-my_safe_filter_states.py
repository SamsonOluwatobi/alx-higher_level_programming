#!/usr/bin/python3
"""Print all states where 'name' matches the input argument.

This script connects to a MySQL database using the provided username, password,
and database name. It then executes a SQL query to select all states from the
'states' table where the 'name' column matches the provided argument, ordering
them by id in ascending order. The results are printed to stdout.

Usage: python3 my_safe_filter_states.py <username><password>
<database><state_name>
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
    cmd = """SELECT id, name
             FROM states
             WHERE name=%s
             ORDER BY id ASC"""
    cur.execute(cmd, (sys.argv[4],))
    nStates = cur.fetchall()

    for state in nStates:
        print(state)

    cur.close()
    db.close()
