# #!/usr/bin/env python
import printer_util
import gpt
from database import Database_Manager

def main():

    printer_util.welcome()

    connection_string = r"DRIVER={ODBC Driver 17 for SQL Server};Server=michael\SQLEXPRESS01;Database=Hotel;Trusted_Connection=yes;"
    output_directory = "XXX"

    db_manager = Database_Manager(connection_string, output_directory)

    printer_util.input(connection_string, output_directory)

    if print_option:
        if tables_option:
            printer_util.print_tables(db_manager)
        elif relationships_option:
            printer_util.print_relationships(db_manager)
        elif order_option:
            printer_util.print_table_order(db_manager)
        else:
            printer_util.print_error()
    elif generate_option:
        gpt.get_response()
    elif write_option:
        db_manager.write_to_output_directory()
    elif abort_option:
        printer_util.print_error("Aborting...")
    else:
        printer_util.print_error()

if __name__ == "__main__":
    main()