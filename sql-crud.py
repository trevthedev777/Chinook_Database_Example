from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# executing the instructions from the "chinook" database
# postgresql:///chinook (We are using the postgres server on our localhost (///) to access the chinook db) # noqa
db = create_engine("postgresql:///chinook")
base = declarative_base()

# Three things we need to do to access and query our db
# =====================================================
# instead of connecting to the databse directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# open an actual session by calling the Session() subclass defined above
session = Session()

# creating the databse using declarative_base subclass
base.metadata.create_all(db)
