#!/usr/bin/python3
"""
a script that lists all State objects
from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    db_url = 'mysql+mysqldb://{}:{}@localhost/{}' \
             .format(argv[1], argv[2], argv[3])
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)

    session = Session()

    for state in session.query(State).order_by(State.id):
        print('{}: {}'.format(state.id, state.name))
    session.close()
