# Data Engine CLI For Microsoft SQL Server

This lightweight CLI is designed to generate test data for your SQL Server database. Just add your API key and connection string to an .env file in the app directory and you're good to go! Using OpenAI GPT models, this application sends prompts with all relevant metadata of your database, along with any user input, resulting in ready-made INSERT statements you can instantly use. Whether you want to copy and paste, write to a file or insert directly into your database is completely up to you.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [License](#license)
- [Credits](#credits)
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

**Note**: copy and paste your connection string and OpenAI API key instead of the placeholder, run program again and you're good to go!

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

## License

[![License](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-blue.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

## Credits

I would like to express my gratitude to the following open-source projects and their contributors, whose work has made my project possible:

- [aiohttp](https://github.com/aio-libs/aiohttp) v3.9.0
- [aiosignal](https://github.com/python-trio/aiosignal) v1.3.1
- [annotated-types](https://github.com/python/peps/pull/1145) v0.6.0
- [anyio](https://github.com/agronholm/anyio) v3.7.1
- [attrs](https://github.com/python-attrs/attrs) v23.1.0
- [certifi](https://github.com/certifi/python-certifi) v2023.11.17
- [charset-normalizer](https://github.com/Drekin/charset_normalizer) v3.3.2
- [click](https://github.com/pallets/click) v8.1.7
- [colorama](https://github.com/tartley/colorama) v0.4.6
- [distro](https://github.com/nir0s/distro) v1.8.0
- [frozenlist](https://github.com/freshcat/frozenlist) v1.4.0
- [greenlet](https://github.com/python-greenlet/greenlet) v3.0.1
- [h11](https://github.com/python-hyper/h11) v0.14.0
- [halo](https://github.com/manrajgrover/halo) v0.0.31
- [httpcore](https://github.com/encode/httpcore) v1.0.2
- [httpx](https://github.com/encode/httpx) v0.25.2
- [idna](https://github.com/kjd/idna) v3.6
- [iniconfig](https://github.com/matrix-org/python-iniconfig) v2.0.0
- [log-symbols](https://github.com/sindresorhus/log-symbols) v0.0.14
- [multidict](https://github.com/aio-libs/multidict) v6.0.4
- [openai](https://github.com/openai/openai) v1.3.7
- [packaging](https://github.com/pypa/packaging) v23.2
- [pluggy](https://github.com/pytest-dev/pluggy) v1.3.0
- [prompt-toolkit](https://github.com/prompt-toolkit/python-prompt-toolkit) v3.0.41
- [pydantic](https://github.com/samuelcolvin/pydantic) v2.5.2
- [pydantic-core](https://github.com/samuelcolvin/pydantic-core) v2.14.5
- [pymssql](https://github.com/pymssql/pymssql) v2.2.11
- [PyMySQL](https://github.com/PyMySQL/PyMySQL) v1.1.0
- [pyodbc](https://github.com/mkleehammer/pyodbc) v5.0.1
- [pytest](https://github.com/pytest-dev/pytest) v7.4.3
- [python-dotenv](https://github.com/theskumar/python-dotenv) v1.0.0
- [regex](https://github.com/python/regex) v2023.10.3
- [requests](https://github.com/psf/requests) v2.31.0
- [six](https://github.com/benjaminp/six) v1.16.0
- [sniffio](https://github.com/python-trio/sniffio) v1.3.0
- [spinners](https://github.com/ionelmc/python-spinners) v0.0.24
- [SQLAlchemy](https://github.com/sqlalchemy/sqlalchemy) v2.0.23
- [termcolor](https://github.com/hfeeki/termcolor) v2.4.0
- [tiktoken](https://github.com/boudinfl/tiktoken) v0.5.2
- [tqdm](https://github.com/tqdm/tqdm) v4.66.1
- [typing-extensions](https://github.com/python/typing) v4.8.0
- [urllib3](https://github.com/urllib3/urllib3) v2.1.0
- [wcwidth](https://github.com/jquast/wcwidth) v0.2.12
- [yarl](https://github.com/aio-libs/yarl) v1.9.3

## Support

1. **GitHub Issues:**
   - [Open an issue](https://github.com/your-username/your-repo/issues) on the GitHub repository to report bugs, request features, or ask questions.

## Badges

![Version](https://img.shields.io/badge/Version-1.0.0-brightgreen.svg)
