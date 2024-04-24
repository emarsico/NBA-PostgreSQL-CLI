# db_connector.py

import psycopg2
from psycopg2.extras import RealDictCursor
from setup_tables import setup_tables

def create_database():
    """
    Creates the 'nba' database if it does not exist and sets up tables.
    """
    conn = psycopg2.connect(
        dbname='postgres',
        user='ellio',
        password='',
        host='localhost'
    )
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = 'nba'")
    exists = cur.fetchone()
    if not exists:
        cur.execute("CREATE DATABASE nba")
        print("Database 'nba' created.")
        cur.close()
        conn.close()

        # Connecting to the new database to set up tables
        conn = psycopg2.connect(
            dbname='nba',
            user='ellio',
            password='',
            host='localhost'
        )
        setup_tables(conn)

    cur.close()
    conn.close()

def get_db_connection():
    """
    Ensures the 'nba' database exists and connects to it.
    """
    create_database()  # Ensure the database exists before connecting
    try:
        conn = psycopg2.connect(
            dbname='nba',
            user='ellio',
            password='',
            host='localhost'
        )
        return conn
    except Exception as e:
        print(f"Database connection failed: {e}")
        return None

