# Import classes from the sqlachemy module
from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

# executing the instructions from our localhost "Chinook" db
#  /// shows we are working in our local environment
db = create_engine("postgresql:///chinook")

# its the data about our tables, and whats in those tables
meta = MetaData(db)

# Create a variable for "Artist" table
artist_table = Table(
    "Artist", meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String)
)

# create variable for "Album" table
# Primary key for this table is "AlbumId"
# ForeignKey for this table is "ArtistId", its needs to be linked 
# to the correct table as a param we route it to the artist_table 
# then the .ArtistId to link the ForeignKey
album_table = Table(
    "Album", meta,
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey("artist_table.ArtistId"))
)

# Create variable for the track table
track_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("artist_table.ArtistId")),
    Column("MediaTypeId", Integer, primary_key=False),
    Column("GenreId", Integer, primary_key=False),
    Column("Composer", String),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    Column("UnitPrice", Float)
)

#  Making the connection
with db.connect() as connection:
    
    # Query 1 - select all records from the "Artist" table
    # select_query = artist_table.select()

    # Query 2 -  select only the "Name" column from the "Artist" Table
    # using .c will allow us to search for a specifil column on the table
    # to select only the specific artist name use the .with_only_columns([specify this column]) # noqa
    # select_query = artist_table.select().with_only_columns([artist_table.c.Name]) # noqa

    # Query 3 - select only 'Queen' from the "Artist" table
    # select_query = artist_table.select().where(artist_table.c.Name == "Queen") # noqa

    # Query 4 - Select only the "ArtistId" #51 from the "Artist" table
    # select_query = artist_table.select().where(artist_table.c.ArtistId == 51)

    # Query 5  - select only the albums with "ArtistId" #51 on the "Album" Table # noqa
    # select_query = artist_table.select().where(album_table.c.ArtistId == 51)

    # Query 6 - select all tracks where the composer is "Queen" from the "Track" table
    select_query = track_table.select().where(track_table.c.Composer == "Queen")
    

    results = connection.execute(select_query)
    for result in results:
        print(result)