# main.py

import click
from csv_processor import read_csv_columns
# from db_connector import get_db_connection  # Uncomment when db_connector is implemented

@click.group()
def cli():
    pass

@click.command()
@click.argument('file_name')
@click.option('--columns', '-c', multiple=True, help='Columns to be extracted from the CSV file.')
def process_csv(file_name, columns):
    """
    Processes a CSV file and extracts specified columns.
    """
    file_path = f'NBACSV/{file_name}'
    df = read_csv_columns(file_path, columns)
    if not df.empty:
        print(df)
    else:
        print("No data found or error reading the file.")

cli.add_command(process_csv)

if __name__ == '__main__':
    cli()
