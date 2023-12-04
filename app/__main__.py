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

    while True:
        user_input = input('> ')
    

if __name__ == "__main__":
    main()