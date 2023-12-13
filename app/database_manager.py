import sqlalchemy
import pyodbc
from sqlalchemy.schema import CreateTable

#DRIVER={ODBC Driver 17 for SQL Server};Server=michael\SQLEXPRESS01;Database=Hotel;Trusted_Connection=yes;
class Database_Manager:
    """A class to manage the database connection and schema extraction."""

    # properties

    connection_string: str
    engine: sqlalchemy.Engine
    inspector = sqlalchemy.Inspector
    metadata: sqlalchemy.MetaData
    db_name: str
    tables: list
    relationships: dict
    table_order: list
    table_props: list

    # constructor

    def __init__(self, connection_string):
        self.set_connection_string(connection_string)
        self.set_engine()
        self.set_inspector()
        self.set_metadata()
        self.set_db_name()
        self.set_tables()
        self.set_relationships()
        self.set_table_order()
        self.set_table_props()

    # setters

    def set_connection_string(self, connection_string):
        self.connection_string = f"mssql+pyodbc:///?odbc_connect=" + connection_string
    def set_engine(self):
        self.engine = sqlalchemy.create_engine(self.connection_string)
    def set_inspector(self):
        self.inspector = sqlalchemy.Inspector.from_engine(self.engine)
    def set_metadata(self):
        self.metadata = sqlalchemy.MetaData()
        self.metadata.reflect(bind=self.engine)
    def set_db_name(self):
        self.db_name = self.connection_string.split(';')[2].split('=')[1]
    def set_tables(self):
        self.tables = self.metadata.tables.values()
    def set_relationships(self):
        # usage of dictionary comprehension
        self.relationships = {table.name: [foreign_key.target_fullname for foreign_key in table.foreign_keys]
                                for table in self.metadata.tables.values()}
    def set_table_order(self):
        """Get the order in which tables should be generated."""
        engine = sqlalchemy.create_engine(self.connection_string)
        inspector = sqlalchemy.Inspector.from_engine(engine)

        # Get tables without foreign keys
        tables_without_foreign_keys = []

        for table_name in inspector.get_table_names():
            foreign_keys = inspector.get_foreign_keys(table_name)
        if not foreign_keys:
            tables_without_foreign_keys.append(table_name)

        # Build the table order
        self.table_order = tables_without_foreign_keys.copy()

        # Get tables with foreign keys
        tables_with_foreign_keys = list(set(inspector.get_table_names()) - set(tables_without_foreign_keys))

        # Add tables with foreign keys in the order of their foreign key dependencies
        while tables_with_foreign_keys:
            table_added = False
            for table in tables_with_foreign_keys.copy():
                foreign_keys = inspector.get_foreign_keys(table)

                # Check if all referred tables are already in the order
                if all(fk['referred_table'] in self.table_order for fk in foreign_keys):
                    self.table_order.append(table)
                    tables_with_foreign_keys.remove(table)
                    table_added = True

            # If no table was added, there might be a circular dependency
            if not table_added:
                raise ValueError("Circular dependency detected in table relationships.")
            
    def set_table_props(self):
        self.table_props = []
        for table_name in self.table_order:
            table = self.metadata.tables[table_name]
            create_table_stmt = str(CreateTable(table).compile(self.engine)).replace('CREATE TABLE', '')
            create_table_stmt = create_table_stmt.replace('(', '')
            create_table_stmt = create_table_stmt.replace(')', '')
            create_table_stmt = create_table_stmt.strip()
            self.table_props.append(create_table_stmt)

    def insert_into_db(self, connection_string, insert_stmt):
        try:
            conn = pyodbc.connect(connection_string)
            with conn as connection:
                cursor = connection.cursor()
                cursor.execute(insert_stmt)
                cursor.commit()
                print('Data succesfully inserted into database.')
        except Exception as e:
            cursor.rollback() 
            print(f"An unexpected error occurred: {e}")