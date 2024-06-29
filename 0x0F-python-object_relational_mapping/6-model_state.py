#!/usr/bin/python3
"""Create link between table in database and Python class

This script creates link between table in database and Python class
from model_state.py.

Usage:
    python3 6-model_state.py <username> <password> <db_name>
"""

import sys

from model_state import Base, State
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
