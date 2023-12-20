# Data Egnine CLI For Microsoft SQL Server

This lightweight CLI is designed to generate test data for your SQL Server database. Just add your API key and connection string to an .env file in the app directory and you're good to go! Using OpenAI GPT models this application sends prompts with all relevant metadata of your database, along with any user input, resulting in ready-made INSERT statements you can use instantly. Wether you want to copy and paste, write to a file or insert directly into your database is completely up to you.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)
- [Credits](#credits)
- [Documentation](#documentation)
- [Tests](#tests)
- [Changelog](#changelog)
- [Support](#support)
- [Acknowledgments](#acknowledgments)
- [Badges](#badges)
- [Demo](#demo)

## Prerequisites

1. [Python](https://www.python.org/downloads/) installed
2. [ODBC Driver for SQL Server](https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver16#download-for-windows) installed

## Installation

1. Clone the repository:

   ```bash
   git clone <link to this repository>
   ```

2. Navigate to the project directory:

   ```bash
   cd your-repository
   ```

3. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   - On Windows:

     ```bash
     .\venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

5. Install project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

**Note**: don't create an .env file just yet. Run the program for the first time, it will create an .env file with placeholders and exit.

6. Now you're ready to run the project:

   ```bash
   python __main__.py
   ```

**Note**:Copy and paste your connection string and OpenAI API key instead of the placeholder, run program again and you're good to go!

## Usage

This is the list of available commands:

Engine-independent commands:

    --help                              see help
    -pt                                 see all tables in the database
    -ptr                                see tables and their FK relationships
    -pto                                see table order for data generation
    --start                             starts engine: keeps prompts, generated data, tables and requirements to memory
    --stop                              stops engine: clears the above from memory
    --models                            see all models
    --setmodel <model_index>            set model
    --getmodel                          get current model
    -q                                  quits the program

Engine-dependent commands:

    -g <number> [-t <table_index>]      specify the number of lines of data data to be generated for each table. Can be used with -t to specify the table index. Table index can be found using -pto command
    -ar <requirement_text>              adds requirement <requirement_text> to the requirement list when engine is running. Prompts are used to customize the data generation output.
    -dr <index>                         deletes requirement <index> from the requirement list when engine is running
    -cr                                 clears requirement list when engine is running
    -pr                                 prints all saved requirements
    -at                                 add table to prompt
    -dt                                 delete table from prompt
    -ct                                 clear tables added to prompt
    -ptp                                see tables added to prompt
    -pp                                 print prompt
    -w <path>                           writes data to file when engine is running
    -idb                                inserts data into database when engine is running

## Configuration

1. Open the ODBC Data Source Administrator:

   - On Windows, search for "ODBC" in the Start menu and choose "ODBC Data Sources (32-bit)" or "ODBC Data Sources (64-bit)" based on your system architecture.
   - On macOS/Linux, use the odbcad32 or odbcad64 command in the terminal.

2. In the ODBC Data Source Administrator, go to the "System DSN" tab.

3. Click "Add" to add a new data source.

4. Select "ODBC Driver 17 for SQL Server" from the list.

5. Configure the connection parameters:

   - Name: Enter a name for your data source.
   - Server: Enter the address of your SQL Server.
   - Authentication: Choose the appropriate authentication method.
   - Database: Enter the name of your database.
   - (Other settings as needed)
   - Test the connection to ensure it's successful.

6. Click "OK" to save the data source.

### Step 1: install ODBC Driver for SQL Server

Go to: https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver16#download-for-windows

### Step 2:

## Contributing

Guidelines for contributing to your project.

## License

Specify the license under which your project is released.

## Credits

Acknowledge any third-party libraries, resources, or contributors.

## Documentation

Link to or include additional documentation or user guides.

## Support

Information on how users can get help or support.

## Acknowledgments

Show appreciation for individuals or organizations that supported or inspired your work.

## Badges

Include badges to showcase project or build status.

## Demo

Link to a live demo or a video demonstrating your app.
