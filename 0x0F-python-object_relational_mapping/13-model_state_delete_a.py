#!/usr/bin/python3
"""Deletes all states with name containing letter 'a' from 'hbtn_0e_6_usa'.

This script requires three command line arguments: a MySQL username, a MySQL
password, and a MySQL database name. It connects to the specified database
using the provided credentials, deletes all states with name containing letter
'a', and commits the changes.
"""

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    states_to_delete = session.query(State).filter(State.name.like('%a%'))
    for state in states_to_delete:
        session.delete(state)

    session.commit()
