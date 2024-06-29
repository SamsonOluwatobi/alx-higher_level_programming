#!/usr/bin/python3
"""Script that lists all State objects that contain letter 'a' from
   the database 'hbtn_0e_6_usa'

The script should take three arguments: username, password and database name
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State


def main():
    """Main function that lists all State objects that contain letter 'a'
       from the database 'hbtn_0e_6_usa'
    """
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}"
        .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    for instance in session.query(State).filter(State.name.like('%a%')):
        print("{}: {}".format(instance.id, instance.name))


if __name__ == "__main__":
    main()
