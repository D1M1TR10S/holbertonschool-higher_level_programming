#!/usr/bin/python3
"""
A script that adds another state to the database
"""

from model_state import Base, State
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(State(name="Louisiana"))
    session.commit()
    for row in session.query(State).order_by(State.id)[-1:]:
        print("{}".format(row.id))
    session.close()
