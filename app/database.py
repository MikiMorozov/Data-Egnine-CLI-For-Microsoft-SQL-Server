import sqlalchemy
from sqlalchemy.schema import CreateTable

#DRIVER={ODBC Driver 17 for SQL Server};Server=michael\SQLEXPRESS01;Database=Hotel;Trusted_Connection=yes;
class Database_Manager:
    """A class to manage the database connection and schema extraction."""

    # properties

    connection_string: str
    output_directory: str
    engine: sqlalchemy.Engine
    inspector = sqlalchemy.Inspector
    metadata: sqlalchemy.MetaData
    tables: list
    relationships: {}
    table_order: []
    # table_props: list

    # constructor

    def __init__(self, connection_string, output_directory):
        self.set_connection_string(connection_string)
        self.set_output_directory(output_directory)
        self.set_engine()
        self.set_metadata()
        self.set_inspector()
        self.set_tables()
        self.set_relationships()
        self.set_table_order()
        self.set_table_props()

    # setters

    def set_connection_string(self, connection_string):
        self.connection_string = f"mssql+pyodbc:///?odbc_connect=" + connection_string
    def set_output_directory(self, output_directory):
        self.output_directory = output_directory
    def set_engine(self):
        self.engine = sqlalchemy.create_engine(self.connection_string)
    def set_metadata(self):
        self.metadata = sqlalchemy.MetaData()
        self.metadata.reflect(bind=self.engine)
    def set_inspector(self):
        self.inspector = sqlalchemy.Inspector.from_engine(self.engine)
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
        """Create a string for the table creation statement."""
        self.table_props = []
        for table_name in self.table_order:
            table = self.metadata.tables[table_name]
            create_table_stmt = str(CreateTable(table).compile(self.engine)).replace('CREATE TABLE', '')
            create_table_stmt = create_table_stmt.replace('(', '')
            create_table_stmt = create_table_stmt.replace(')', '')
            create_table_stmt = create_table_stmt.strip()
            self.table_props.append(create_table_stmt)