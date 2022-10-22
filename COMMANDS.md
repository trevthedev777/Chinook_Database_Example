# 01 - Installing the Chinook Database

---

### Download the Chinook PostgreSql database
- [source](https://github.com/lerocha/chinook-database/blob/master/ChinookDatabase/DataSources/Chinook_PostgreSql.sql)
- `wget https://raw.githubusercontent.com/lerocha/chinook-database/master/ChinookDatabase/DataSources/Chinook_PostgreSql.sql`

### Access the Postgres CLI
- `psql`

### Create the new "chinook" database
- `CREATE DATABASE chinook;`

### View existing tables on the database
- `\l`

### Switch between databases
- `\c postgres` (switch to the database called "postgres")
- `\c chinook` (switch to the database called "chinook")

### Install / Initialize the downloaded Chinook SQL database
- `\i Chinook_PostgreSql.sql` (takes several minutes)

# 02 - PostgreSQL from the Command Line

---

### Quit the entire Postgres CLI
- `\q`

### Connect to the "chinook" Postgres CLI database
- `psql -d chinook`

### Display all tables on the "chinook" database
- `\dt`

### Quit the query / return back to CLI after a query
- `q`

### Retrieve all data from the "Artist" table
- `SELECT * FROM "Artist";`

### Retrieve only the "Name" column from the "Artist" table
- `SELECT "Name" FROM "Artist";`

### Retrieve only "Queen" from the "Artist" table
- `SELECT * FROM "Artist" WHERE "Name" = 'Queen';`

### Retrieve only "Queen" from the "Artist" table, but using the "ArtistId" of '51'
- `SELECT * FROM "Artist" WHERE "ArtistId" = 51;`

### Retrieve all albums from the "Album" table, using the "ArtistId" of '51'
- `SELECT * FROM "Album" WHERE "ArtistId" = 51;`

### Retrieve all tracks from the "Track" table, using the "Composer" of 'Queen'
- `SELECT * FROM "Track" WHERE "Composer" = 'Queen';`

---

## OPTIONAL

### Copy the results into a .CSV file
- `\copy (SELECT * FROM "Track" WHERE "Composer" = 'Queen') TO 'test.csv' WITH CSV DELIMITER ',' HEADER;`

### Copy the results into a .JSON file
- Line 1: `\o test.json`
- Line 2: `SELECT json_agg(t) FROM  (SELECT * FROM "Track" WHERE "Composer" = 'Queen') t;`

# 03 - Installing the Libraries and Setting Up

---

### Install the "psycopg2" Python package
- `pip3 install psycopg2`

### Create a new file: "sql-psycopg2.py"
- `touch sql-psycopg2.py`

# 04 - Introducing an ORM

## What is it? 
- An object-relational mapper.

## What does it do?
- Bridges the gap between Python objects and Postgres Tables

## How do you use it?
- Query and manipulate a database using Python, instead of raw SQL commands

The most popular `ORM` frameworks are `Django` and `SQL Alchemy`, they work really well with `Postgres`
---

### Install the "SQLAlchemy" Python package
- `pip3 install SQLAlchemy`

# 05 - Running Basic Queries

## What is it?
-   SQLAlchemy's middle abstraction layer, the Expression Language (Allows us to query the database using Python code)

## What does it do?
- Simplifies queries to the databse using tables

## How do you use it?
- Connect Python and the SQLAlchemy library to the databse, using cleaner code.


---

### Create a new file called "sql-expression.py"
- `touch sql-expression.py`

### Query 1 - select all records from the "Artist" table
- `select_query = artist_table.select()`

### Query 2 - select only the "Name" column from the "Artist" table
- `select_query = artist_table.select().with_only_columns([artist_table.c.Name])`

### Query 3 - select only 'Queen' from the "Artist" table
- `select_query = artist_table.select().where(artist_table.c.Name == "Queen")`

### Query 4 - select only by 'ArtistId' #51 from the "Artist" table
- `select_query = artist_table.select().where(artist_table.c.ArtistId == 51)`

### Query 5 - select only the albums with 'ArtistId' #51 on the "Album" table
- `select_query = album_table.select().where(album_table.c.ArtistId == 51)`

### Query 6 - select all tracks where the composer is 'Queen' from the "Track" table
- `select_query = track_table.select().where(track_table.c.Composer == "Queen")`

# 06 - Introducing Class-Based Models

## What is a Class-based model

- A collection of __methods__ that serve a common purpose, with each __method__ having its own purpose

---

### Create a new file called "sql-orm.py"
- `touch sql-orm.py`

### Query 1 - select all records from the "Artist" table
```python
artists = session.query(Artist)
for artist in artists:
    print(artist.ArtistId, artist.Name, sep=" | ")
```

### Query 2 - select only the "Name" column from the "Artist" table
```python
artists = session.query(Artist)
for artist in artists:
    print(artist.Name)
```

### Query 3 - select only "Queen" from the "Artist" table
```python
artist = session.query(Artist).filter_by(Name="Queen").first()
print(artist.ArtistId, artist.Name, sep=" | ")
```

### Query 4 - select only by "ArtistId" #51 from the "Artist" table
```python
artist = session.query(Artist).filter_by(ArtistId=51).first()
print(artist.ArtistId, artist.Name, sep=" | ")
```

### Query 5 - select only the albums with "ArtistId" #51 on the "Album" table
```python
albums = session.query(Album).filter_by(ArtistId=51)
for album in albums:
    print(album.AlbumId, album.Title, album.ArtistId, sep=" | ")
```

### Query 6 - select all tracks where the composer is "Queen" from the "Track" table
```python
tracks = session.query(Track).filter_by(Composer="Queen")
for track in tracks:
    print(
        track.TrackId,
        track.Name,
        track.AlbumId,
        track.MediaTypeId,
        track.GenreId,
        track.Composer,
        track.Milliseconds,
        track.Bytes,
        track.UnitPrice,
        sep=" | "
    )
```