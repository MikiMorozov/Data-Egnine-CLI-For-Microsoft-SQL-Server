from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.engine.reflection import Inspector
from collections import deque
import click

#DRIVER={ODBC Driver 17 for SQL Server};Server=michael\SQLEXPRESS01;Database=Hotel;Trusted_Connection=yes;

def extract_database_schema(connection_string):
    """Extract the database schema including tables and their relationships."""
    engine = create_engine(f'mssql+pyodbc:///?odbc_connect={connection_string}')
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

# def get_foreign_keys(inspector, table_name):
#     """Get the foreign keys for the given table."""
#     return inspector.get_foreign_keys(table_name)

# def topological_sort(graph):
#     """Sort the tables by dependencies."""

# def topological_sort(graph):
#     # Modified Kahn's algorithm for topological sorting
#     in_degree = {vertex: 0 for vertex in graph}
#     for vertex in graph:
#         for neighbor in graph[vertex]:
#             in_degree[neighbor] += 1

#     queue = deque(vertex for vertex in graph if in_degree[vertex] == 0)
#     result = []

#     while queue:
#         current_vertex = queue.popleft()
#         result.append(current_vertex)

#         for neighbor in graph[current_vertex]:
#             in_degree[neighbor] -= 1
#             if in_degree[neighbor] == 0:
#                 queue.append(neighbor)

#     return result

# def get_table_order(connection_string):
#     engine = create_engine(f'mssql+pyodbc:///?odbc_connect={connection_string}')
#     inspector = Inspector.from_engine(engine)

#     # Get all table names
#     tables = inspector.get_table_names()

#     # Build a graph of foreign key relationships
#     graph = {table: [fk['referred_table'] for fk in get_foreign_keys(inspector, table)] for table in tables}

#     # Perform topological sorting
#     order = topological_sort(graph)

#     # Print out the order
#     click.echo(click.style("Table Order:", fg='green'))
#     for i, table_name in enumerate(order, start=1):
#         print(f"{i}. {table_name}")

#     return order

def get_tables_without_foreign_keys(inspector):
    # Get tables without foreign keys
    tables = inspector.get_table_names()
    tables_without_foreign_keys = []

    for table in tables:
        foreign_keys = inspector.get_foreign_keys(table)
        if not foreign_keys:
            tables_without_foreign_keys.append(table)

    return tables_without_foreign_keys

def get_table_order(connection_string):
    engine = create_engine(f'mssql+pyodbc:///?odbc_connect={connection_string}')
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

    return table_order

