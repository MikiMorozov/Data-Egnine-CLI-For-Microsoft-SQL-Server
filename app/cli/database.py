import sqlalchemy
from sqlalchemy.engine.reflection import Inspector
from collections import deque
import click


#DRIVER={ODBC Driver 17 for SQL Server};Server=michael\SQLEXPRESS01;Database=Hotel;Trusted_Connection=yes;
class Database_Manager:
    """A class to manage the database connection and schema extraction."""

    # properties

    connection_string: str
    output_directory: str
    engine: sqlalchemy.Engine
    inspector = sqlalchemy.Inspector
    metadata: sqlalchemy.MetaData()
    tables: list
    relationships: {}
    table_order: list

    # constructor

    def __init__(self, connection_string, output_directory):
        self.set_connection_string(connection_string)
        self.set_output_directory(output_directory)
        self.set_engine(self)
        self.set_metadata(self)
        self.set_inspector(self)
        self.set_tables(self)
        self.set_relationships(self)
        self.set_table_order(self)

    # setters

    def set_connection_string(self, connection_string):
        self.connection_string = f"mssql+pyodbc:///?odbc_connect=" + connection_string
    def set_output_directory(self, output_directory):
        self.output_directory = output_directory
    def set_engine(self):
        self.engine = sqlalchemy.create_engine(self.connection_string)
    def set_metadata(self):
        self.metadata = self.metadata.reflect(bind=self.engine)
    def set_inspector(self):
        self.inspector = Inspector.from_engine(self.engine)
    def set_tables(self):
        self.tables = self.metadata.tables.values()
    def set_relationships(self):
        # usage of dictionary comprehension
        self.relationships = {table.name: [foreign_key.target_fullname for foreign_key in table.foreign_keys]
                                for table in self.metadata.tables.values()}
    def set_table_order(self, table_order):
        self.table_order = table_order

    # methods

    def print_database_schema(self):
        """Extract the database schema including tables and their relationships."""

        # Print table names
        click.echo(click.style("Tables:", fg='green'))

        for i, table in enumerate(self.tables, start=1):
            print(f"{i}. {table.name}")

        # Print relationships
        click.echo(click.style("\nTable relationships:", fg='green'))
        for table_name, foreign_keys in self.relationships.items():
            for foreign_key in foreign_keys:
                print(f"{table_name} -> {foreign_key.target_fullname}")


    def get_tables_without_foreign_keys(inspector):
        # Get tables without foreign keys
        tables = inspector.get_table_names()
        tables_without_foreign_keys = []

        for table in tables:
            foreign_keys = inspector.get_foreign_keys(table)
            if not foreign_keys:
                tables_without_foreign_keys.append(table)

        return tables_without_foreign_keys

    def get_table_order(self):
        """Get the order in which tables should be generated."""
        engine = sqlalchemy.create_engine(self.connection_string)
        inspector = Inspector.from_engine(engine)

        # Get tables without foreign keys
        tables_without_foreign_keys = self.get_tables_without_foreign_keys(inspector)

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