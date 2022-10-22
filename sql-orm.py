from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# executing the instructions from the "chinook" database
# postgresql:///chinook (We are using the postgres server on our localhost (///) to access the chinook db) # noqa
db = create_engine("postgresql:///chinook")
base = declarative_base()


# Create a class-based model for the "Artist" table
class Artist(base):
    __tablename__ = "Artist"
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)


# Create a class-based Model for the "Album" table
class Album(base):
    __tablename__ = "Album"
    AlbumId: Column(Integer, primary_key=True)
    Title: Column(String)
    ArtistId: Column(Integer)


# Create a class-based model for the "Track" table
class Track(base):
    __tablename__ = "Track"
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey("Album.AlbumId"))
    MediaTypeId = Column(Integer, primary_key=False)
    GenreId = Column(Integer, primary_key=False)
    Composer = Column(String)
    Milliseconds = Column(Integer, primary_key=False)
    Bytes = Column(Integer, primary_key=False)
    UnitPrice = Column(Float)


# Three things we need to do to access and query our db
# =====================================================
# instead of connecting to the databse directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# open an actual session by calling the Session() subclass defined above
session = Session()

# creating the databse using declarative_base subclass
base.metadata.create_all(db)


#  Query 1 - select all the records from the "Artist" table
artists = session.query(Artist)
for artist in artists:
    print(artist.ArtistId, artist.Name, sep="|")
