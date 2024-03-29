#!/usr/bin/python3
"""
a script that creates the State “California” with
the City “San Francisco” from the database hbtn_0e_100_usa
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    db_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()
    new_state = State(name="California")
    cities = [City(name="San Francisco")]
    new_state.cities = cities
    session.add(new_state)
    session.commit()
    session.close()
