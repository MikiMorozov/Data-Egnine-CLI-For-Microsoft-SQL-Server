from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.engine.reflection import Inspector
from collections import deque
import click

CONNECTION_STRING = f"mssql+pyodbc:///?odbc_connect="
OUTPUT_DIRECTORY = ""
TABLE_ORDER = []

#DRIVER={ODBC Driver 17 for SQL Server};Server=michael\SQLEXPRESS01;Database=Hotel;Trusted_Connection=yes;

def extract_database_schema():
    """Extract the database schema including tables and their relationships."""
    engine = create_engine(CONNECTION_STRING)
    metadata = MetaData()
    metadata.reflect(bind=engine)

    # Print table names
    click.echo(click.style("Tables:", fg='green'))
    for i, table in enumerate(metadata.tables.values(), start=1):
        print(f"{i}. {table.name}")

    # Print relationships
    click.echo(click.style("\nTable relationships:", fg='green'))
    for table in metadata.tables.values():
        for foreign_key in table.foreign_keys:
            print(f"{table.name} -> {foreign_key.target_fullname}")

def get_tables_without_foreign_keys(inspector):
    # Get tables without foreign keys
    tables = inspector.get_table_names()
    tables_without_foreign_keys = []

    for table in tables:
        foreign_keys = inspector.get_foreign_keys(table)
        if not foreign_keys:
            tables_without_foreign_keys.append(table)

    return tables_without_foreign_keys

def get_table_order():
    global TABLE_ORDER

    engine = create_engine(CONNECTION_STRING)
    inspector = Inspector.from_engine(engine)

    # Get tables without foreign keys
    tables_without_foreign_keys = get_tables_without_foreign_keys(inspector)

    # Build the table order
    table_order = tables_without_foreign_keys.copy()

    # Get tables with foreign keys
    tables_with_foreign_keys = list(set(inspector.get_table_names()) - set(tables_without_foreign_keys))

    # Add tables with foreign keys in the order of their foreign key dependencies
    while tables_with_foreign_keys:
        table_added = False
        for table in tables_with_foreign_keys.copy():
            foreign_keys = inspector.get_foreign_keys(table)

            # Check if all referred tables are already in the order
            if all(fk['referred_table'] in table_order for fk in foreign_keys):
                table_order.append(table)
                tables_with_foreign_keys.remove(table)
                table_added = True

        # If no table was added, there might be a circular dependency
        if not table_added:
            raise ValueError("Circular dependency detected in table relationships.")

    # Print out the order
    click.echo(click.style("\nTable order for data generation:", fg='green'))
    for i, table_name in enumerate(table_order, start=1):
        print(f"{i}. {table_name}")

    TABLE_ORDER = table_order