#!/usr/bin/python3
"""
Start link class to table in database
A script that deletes all State objects with a name containing the letter a
from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()

    instance = session.query(State).filter(State.name.contains('a')).all()

    for state in instance:
        session.delete(state)
    session.commit()

    session.close()