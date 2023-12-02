# #!/usr/bin/env python
import gpt
import click
import cli.database

# from app.cli.commands import generate_dummy_data

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.command(context_settings=CONTEXT_SETTINGS)
def main():
    click.clear()
    """Welcome to the Dummy Data Generator CLI.

    This program generates dummy data for your application.
    """
    click.echo("****************************************")
    click.echo("Welcome to the Dummy Data Generator CLI.")
    click.echo("****************************************")
    click.echo("This program generates dummy data for your application.")


    # cli.database.CONNECTION_STRING += click.prompt('Please provide the connection string for your database')
                         
    # cli.database.OUTPUT_DIRECTORY = click.prompt("Please provide the output directory for the generated data")

    cli.database.CONNECTION_STRING += r"DRIVER={ODBC Driver 17 for SQL Server};Server=michael\SQLEXPRESS01;Database=Hotel;Trusted_Connection=yes;"
    cli.database.OUTPUT_DIRECTORY = "XXX"

    # Now you can use the provided input (connection_string, output_dir) as needed

    click.echo("----------------------------------------")
    click.echo(f"Connection String: {cli.database.CONNECTION_STRING}")
    click.echo(f"Output Directory: {cli.database.OUTPUT_DIRECTORY}")
    click.echo("----------------------------------------")

    cli.database.extract_database_schema()
    cli.database.get_table_order()

    click.confirm("\nStart generating data?", abort=True)

    # create list of all tables in the database
    

    gpt.get_response()

if __name__ == "__main__":
    main()