#!/usr/bin/python3
"""
write a script that prints all City objects
from the database hbtn_0e_14_usa
"""

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)

    session = Session()
    results = session.query(State.name, City.id, City.name)\
                     .join(City, City.state_id == State.id)\
                     .order_by(City.id)
    for result in results:
        print("{}: ({}) {}".format(result[0], result[1], result[2]))

    session.commit()
    session.close()
