# csv_processor.py

import pandas as pd

def read_csv_columns(file_path, columns):
    """
    Reads specified columns from a CSV file.
    
    Parameters:
        file_path (str): The path to the CSV file.
        columns (list): A list of column names to read.
        
    Returns:
        pd.DataFrame: A DataFrame containing the specified columns.
    """
    try:
        df = pd.read_csv(file_path, usecols=columns)
        return df
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return pd.DataFrame()
