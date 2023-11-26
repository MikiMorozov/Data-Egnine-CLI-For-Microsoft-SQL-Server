from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.engine.reflection import Insector
from collections import deque
import click

#DRIVER={ODBC Driver 17 for SQL Server};Server=michael\SQLEXPRESS01;Database=Hotel;Trusted_Connection=yes;

def extract_database_schema(connection_string):
    """Extract the database schema including tables and their relationships."""
    engine = create_engine(f'mssql+pyodbc:///?odbc_connect={connection_string}')
    metadata = MetaData()
    metadata.reflect(bind=engine)

    # Print table names
    click.echo(click.style("Tables", fg='green'))
    for table in metadata.tables.values():
        print(f"- {table.name}")

    # Print relationships
    click.echo(click.style("\nTable Relationships:", fg='green'))
    for table in metadata.tables.values():
        for foreign_key in table.foreign_keys:
            print(f"{table.name} -> {foreign_key.target_fullname}")

def sort_tables_by_dependencies(tables):
    """Sort the tables by dependencies."""
    

