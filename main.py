# main.py

from db_connector import get_db_connection
from logging_function import log_query
import psycopg2


# Utility function to connect and get a cursor
def get_cursor(conn):
    return conn.cursor()

def insert_data():
    """
    Insert data into a table, with table name, columns, and values specified by the user.
    """
    try:
        table_name = input("Enter the table name: ")
        columns = input("Enter the column names separated by commas (e.g., Column1,Column2): ")
        values_input = input("Enter the values in the same order as columns separated by commas (e.g., Value1,Value2): ")
        values = tuple(values_input.split(','))
        
        conn = get_db_connection()
        cur = conn.cursor()
        query = f"INSERT INTO {table_name} ({columns}) VALUES (%s, %s)"  # Use formatting for table and column names, parameterized query for values
        cur.execute(query, values)
        conn.commit()
        log_query(cur.mogrify(query, values).decode('utf-8'))
        print("Data inserted successfully.")
    except Exception as e:
        print(f"An error occurred during insert operation: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

def delete_data():
    """
    Delete specific records from a table based on user-specified conditions.
    """
    try:
        table_name = input("Enter the table name: ")
        condition = input("Enter the condition for deletion (e.g., Column = 'Value'): ")
        
        conn = get_db_connection()
        cur = conn.cursor()
        query = f"DELETE FROM {table_name} WHERE {condition}"
        cur.execute(query)
        conn.commit()
        log_query(cur.mogrify(query).decode('utf-8'))
        print("Data deleted successfully.")
    except Exception as e:
        print(f"An error occurred during delete operation: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

def update_data():
    """
    Modify existing records in a table based on user input.
    """
    try:
        table_name = input("Enter the table name: ")
        set_clause = input("Enter the column and new value to set (e.g., Column = 'NewValue'): ")
        condition = input("Enter the condition for the update (e.g., ConditionColumn = 'ConditionValue'): ")
        
        conn = get_db_connection()
        cur = conn.cursor()
        query = f"UPDATE {table_name} SET {set_clause} WHERE {condition}"
        cur.execute(query)
        conn.commit()
        log_query(cur.mogrify(query).decode('utf-8'))
        print("Data updated successfully.")
    except Exception as e:
        print(f"An error occurred during update operation: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

def search_data():
    """
    Find records based on specified criteria provided by the user.
    """
    try:
        table_name = input("Enter the table name: ")
        condition = input("Enter the search condition (e.g., Column = 'Value'): ")
        
        conn = get_db_connection()
        cur = conn.cursor()
        query = f"SELECT * FROM {table_name} WHERE {condition}"
        cur.execute(query)
        records = cur.fetchall()
        for record in records:
            print(record)
        log_query(query)
    except Exception as e:
        print(f"An error occurred during search operation: {e}")
    finally:
        cur.close()
        conn.close()

def aggregate_functions():
    """
    Perform calculations like sum, average, count, min, and max, based on user input.
    """
    try:
        table_name = input("Enter the table name: ")
        column_name = input("Enter the column name for aggregation: ")
        agg_function = input("Enter the aggregate function to perform (SUM, AVG, COUNT, MIN, MAX): ")
        
        conn = get_db_connection()
        cur = conn.cursor()
        query = f"SELECT {agg_function}({column_name}) FROM {table_name}"
        cur.execute(query)
        result = cur.fetchone()
        print(f"{agg_function} of {column_name}: ", result[0])
        log_query(query)
    except Exception as e:
        print(f"An error occurred during aggregate functions operation: {e}")
    finally:
        cur.close()
        conn.close()

def joins():
    """
    Combine data from multiple tables using relationships, based on user input.
    """
    try:
        table1_name = input("Enter the first table name: ")
        table2_name = input("Enter the second table name: ")
        join_condition = input("Enter the join condition (e.g., Table1.Column = Table2.Column): ")
        
        conn = get_db_connection()
        cur = conn.cursor()
        query = f"SELECT * FROM {table1_name} INNER JOIN {table2_name} ON {join_condition}"
        cur.execute(query)
        joined_data = cur.fetchall()
        for data in joined_data:
            print(data)
        log_query(query)
    except Exception as e:
        print(f"An error occurred during join operation: {e}")
    finally:
        cur.close()
        conn.close()

def grouping():
    """
    Group query results based on specified columns, as provided by the user,
    optionally performing an aggregate function.
    """
    try:
        table_name = input("Enter the table name: ")
        group_by_column = input("Enter the column name(s) to group by (e.g., Column1, Column2): ")
        agg_function = input("Optional - Enter the aggregate function and column (e.g., COUNT(Column3), leave blank if not applicable): ")
        
        conn = get_db_connection()
        cur = conn.cursor()
        if agg_function:
            query = f"SELECT {group_by_column}, {agg_function} FROM {table_name} GROUP BY {group_by_column}"
        else:
            query = f"SELECT * FROM {table_name} GROUP BY {group_by_column}"
        
        cur.execute(query)
        grouped_data = cur.fetchall()
        for data in grouped_data:
            print(data)
        log_query(query)
    except Exception as e:
        print(f"An error occurred during grouping operation: {e}")
    finally:
        cur.close()
        conn.close()

def subqueries():
    """
    Execute a query that includes a subquery, with all parts specified by the user.
    """
    try:
        main_query = input("Enter the main query, using '(SUBQUERY)' where the subquery should be inserted:\n")
        subquery = input("Enter the subquery:\n")
        
        full_query = main_query.replace('(SUBQUERY)', f"({subquery})")
        
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(full_query)
        subquery_results = cur.fetchall()
        for result in subquery_results:
            print(result)
        log_query(full_query)
    except Exception as e:
        print(f"An error occurred during subquery operation: {e}")
    finally:
        cur.close()
        conn.close()

def transactions():
    """
    Ensure consistency and reliability of database operations by executing a series of user-defined operations within a transaction.
    """
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        conn.autocommit = False

        num_operations = int(input("Enter the number of operations in the transaction: "))
        operations = []

        for i in range(num_operations):
            operation = input(f"Enter SQL operation {i + 1}: ")
            operations.append(operation)

        for operation in operations:
            cur.execute(operation)

        conn.commit()
        print("Transaction completed successfully.")
        for operation in operations:
            log_query(operation)  
    except Exception as e:
        conn.rollback()
        print(f"Transaction failed and has been rolled back: {e}")
    finally:
        conn.autocommit = True
        cur.close()
        conn.close()


def error_handling():
    """
    Catch and handle exceptions gracefully during database operations, with enhanced logging and feedback.
    """
    try:
        # Placeholder for an operation that might fail
        conn = get_db_connection()
        cur = conn.cursor()
        operation = input("Enter the SQL command to execute: ")
        cur.execute(operation)
    except psycopg2.DatabaseError as e:
        print(f"Database error occurred: {e}")
        log_query(f"Database error occurred: {e}")  # Logging the error
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        log_query(f"Unexpected error occurred: {e}")  # Logging the error
    finally:
        cur.close()
        conn.close()

#

#

#

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

