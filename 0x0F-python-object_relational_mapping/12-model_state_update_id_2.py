#!/usr/bin/python3
"""Update state name in the 'hbtn_0e_6_usa' database.

Change name of state with id == 2 to 'New Mexico'.
Script accepts 3 command line arguments: username, password, and database name.
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

    state_to_update = session.query(State).filter(State.id == 2).one()
    state_to_update.name = "New Mexico"

    session.commit()
