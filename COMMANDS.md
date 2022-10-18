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