#!/usr/bin/python3
"""Print all states with a name starting with 'N'
The script must accept 3 arguments: the username, the password
and the database name
"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to the database
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         host='localhost',
                         port=3306)
    cur = db.cursor()
    cmd = """SELECT id, name FROM states WHERE
    name LIKE BINARY 'N%' ORDER BY id ASC;"""
    cur.execute(cmd)
    nStates = cur.fetchall()

    # Print the states with a name starting with 'N'
    for state in nStates:
        print(state)

    cur.close()
    db.close()
