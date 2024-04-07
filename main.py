# main.py

import click
from db_connector import get_db_connection

# Utility function to connect and get a cursor
def get_cursor(conn):
    return conn.cursor()

def insert_data():
    """
    Insert data into a table.
    """
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        # Replace with actual INSERT statement and values
        cur.execute("INSERT INTO TableName (Column1, Column2) VALUES (%s, %s)", ('Value1', 'Value2'))
        conn.commit()
        print("Data inserted successfully.")
    except Exception as e:
        print(f"An error occurred during insert operation: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

def delete_data():
    """
    Delete specific records from a table.
    """
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        # Replace with actual DELETE statement and condition
        cur.execute("DELETE FROM TableName WHERE Condition")
        conn.commit()
        print("Data deleted successfully.")
    except Exception as e:
        print(f"An error occurred during delete operation: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

def update_data():
    """
    Modify existing records in a table.
    """
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        # Replace with actual UPDATE statement, new values, and condition
        cur.execute("UPDATE TableName SET Column1 = %s WHERE Condition", ('NewValue',))
        conn.commit()
        print("Data updated successfully.")
    except Exception as e:
        print(f"An error occurred during update operation: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

def search_data():
    """
    Find records based on specified criteria.
    """
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        # Replace with actual SELECT statement and condition
        cur.execute("SELECT * FROM TableName WHERE Condition")
        records = cur.fetchall()
        for record in records:
            print(record)
    except Exception as e:
        print(f"An error occurred during search operation: {e}")
    finally:
        cur.close()
        conn.close()

def aggregate_functions():
    """
    Perform calculations like sum, average, count, min, and max.
    """
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        # Replace with actual SELECT AGGREGATE statement
        cur.execute("SELECT SUM(Column) FROM TableName")
        sum_value = cur.fetchone()
        print("Sum:", sum_value)
    except Exception as e:
        print(f"An error occurred during aggregate functions operation: {e}")
    finally:
        cur.close()
        conn.close()

def sorting():
    """
    Arrange query results based on specified columns.
    """
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        # Replace with actual SELECT statement with ORDER BY
        cur.execute("SELECT * FROM TableName ORDER BY Column ASC")
        sorted_records = cur.fetchall()
        for record in sorted_records:
            print(record)
    except Exception as e:
        print(f"An error occurred during sorting operation: {e}")
    finally:
        cur.close()
        conn.close()

def joins():
    """
    Combine data from multiple tables using relationships.
    """
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        # Replace with actual JOIN statement
        cur.execute("SELECT * FROM Table1 INNER JOIN Table2 ON Table1.Key = Table2.Key")
        joined_data = cur.fetchall()
        for data in joined_data:
            print(data)
    except Exception as e:
        print(f"An error occurred during join operation: {e}")
    finally:
        cur.close()
        conn.close()

def grouping():
    """
    Group query results based on specified columns.
    """
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        # Replace with actual SELECT statement with GROUP BY
        cur.execute("SELECT Column, COUNT(*) FROM TableName GROUP BY Column")
        grouped_data = cur.fetchall()
        for data in grouped_data:
            print(data)
    except Exception as e:
        print(f"An error occurred during grouping operation: {e}")
    finally:
        cur.close()
        conn.close()

def subqueries():
    """
    Support nested operations within queries.
    """
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        # Replace with actual SELECT statement with a subquery
        cur.execute("SELECT * FROM TableName WHERE Column IN (SELECT Column FROM AnotherTable)")
        subquery_results = cur.fetchall()
        for result in subquery_results:
            print(result)
    except Exception as e:
        print(f"An error occurred during subquery operation: {e}")
    finally:
        cur.close()
        conn.close()

def transactions():
    """
    Ensure consistency and reliability of database operations.
    """
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        conn.autocommit = False
        # Replace with actual database operations that form a transaction
        cur.execute("BEGIN TRANSACTION;")
        # Perform one or more operations; e.g., cur.execute(...)
        conn.commit()
        print("Transaction completed successfully.")
    except Exception as e:
        conn.rollback()
        print(f"Transaction failed and has been rolled back: {e}")
    finally:
        conn.autocommit = True
        cur.close()
        conn.close()

def error_handling():
    """
    Catch and handle exceptions gracefully during database operations.
    """
    try:
        # Assume an operation that might fail
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("...")
    except psycopg2.DatabaseError as e:
        print(f"Database error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        cur.close()
        conn.close()



# Main

def main_menu():
    while True:
        print("""
Welcome to the Database CLI Interface!

Please select an option:
1. Insert Data
2. Delete Data
3. Update Data
4. Search Data
5. Aggregate Functions
6. Sorting
7. Joins
8. Grouping
9. Subqueries
10. Transactions
11. Error Handling
12. Exit
""")
        choice = input("Enter your choice (1-12): ")

        if choice == '1':
            insert_data()
        elif choice == '2':
            delete_data()
        elif choice == '3':
            update_data()
        elif choice == '4':
            search_data()
        elif choice == '5':
            aggregate_functions()
        elif choice == '6':
            sorting()
        elif choice == '7':
            joins()
        elif choice == '8':
            grouping()
        elif choice == '9':
            subqueries()
        elif choice == '10':
            transactions()
        elif choice == '11':
            error_handling() 
        elif choice == '12':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == '__main__':
    main_menu()

