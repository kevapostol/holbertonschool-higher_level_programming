#!/usr/bin/python3
"""
Start link class to table in database
a script that prints the State object with the name passed as argument from the
database hbtn_0e_6_usa
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

    instance = session.query(State).filter(State.name == sys.argv[4]).first()

    if instance is not None:
        print("{}".format(instance.id))
    else:
        print("Not found")

    session.close()
