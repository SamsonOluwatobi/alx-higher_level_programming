#!/usr/bin/python3
"""This script fetches all City objects from the specified database and
prints them in ascending order by their id. The fetched cities
are accompanied by their respective state names.

The script accepts three command line arguments: a MySQL username, a MySQL
password, and a MySQL database name. It uses SQLAlchemy ORM to connect to the
specified database and fetch all City objects. The fetched cities are then
printed in the format "<state name>: (<city id>) <city name>".
"""

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    for state, city in session.query(State,
                                     City).filter(State.id == City.state_id):
        print("{}: ({:d}) {}".format(state.name, city.id, city.name))
