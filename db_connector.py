# db_connector.py

import psycopg2
from psycopg2.extras import RealDictCursor

def get_db_connection():
    """
    Creates a connection to the PostgreSQL database.
    
    Returns:
        conn: A connection object to the PostgreSQL database.
    """
    try:
        conn = psycopg2.connect(
            dbname='your_dbname', 
            user='your_username', 
            password='your_password', 
            host='localhost'
        )
        return conn
    except Exception as e:
        print(f"Database connection failed: {e}")
        return None
