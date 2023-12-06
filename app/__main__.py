# #!/usr/bin/env python
import printer_util
import gpt
import commands
from database import Database_Manager

def main():

    printer_util.welcome()

    connection_string = r"DRIVER={ODBC Driver 17 for SQL Server};Server=michael\SQLEXPRESS01;Database=Hotel;Trusted_Connection=yes;"
    output_directory = "XXX"

    db_manager = Database_Manager(connection_string, output_directory)

    printer_util.input(connection_string, output_directory)


    for string in db_manager.table_props:
        print(string)

    while True:
        user_input = input('> ')
        if user_input == commands.PRINT_HELP:
            printer_util.print_help()
        elif user_input == commands.PRINT_TABLES:
            printer_util.print_tables(db_manager)
        elif user_input == commands.PRINT_TABLE_RELATIONSHIPS:
            printer_util.print_table_relationships(db_manager)
        elif user_input == commands.PRINT_TABLE_ORDER:
            printer_util.print_table_order(db_manager)
        elif user_input == commands.START_DATA_ENGINE:
            print(gpt.get_response())
        elif user_input == commands.WRITE_DATA:
            gpt.write_data(db_manager)
        elif user_input == commands.ABORT:
            break

if __name__ == "__main__":
    main()