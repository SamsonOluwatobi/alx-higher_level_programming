#!/usr/bin/python3
"""This script fetches all State objects from the 'hbtn_0e_6_usa' database
using SQLAlchemy ORM.

The script accepts three command line arguments: a MySQL username, a MySQL
password, and a MySQL database name. It connects to the specified database
using the provided credentials and prints all State objects to the console,
formatted as "<state_id>: <state_name>".
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

    for state in session.query(State).all():
        print("{:d}: {}".format(state.id, state.name))
