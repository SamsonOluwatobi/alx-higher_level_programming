#!/usr/bin/python3
"""Print the State id based on the name argument

This script connects to a MySQL database using the provided username, password,
and database name. It then executes a SQL query to select the id of the State
object where the name column matches the provided argument. If no matching
State object is found, the script prints "Not found".

Usage: ./10-model_state_my_get.py <username> <password> <database> <state_name>
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    res = session.query(State.id).filter(State.name == sys.argv[4])

    if res.first() is None:
        print("Not found")
    else:
        print(res.scalar())
