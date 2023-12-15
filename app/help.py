HELP_TEXT = """

    The following options are available:

    --help                              see help
    -pt                                 see all tables in the database
    -ptr                                see tables and their FK relationships
    -pto                                see table order for data generation
    -pr                                 prints all saved requirements
    -start                              starts engine: saves latest prompt in memory
    -stop                               stops engine: clears latest generated data and prompts from memory
    -w <path>                           writes data to file when engine is running
    -idb                                inserts data into database when engine is running
    -g <number>                         specify the number of lines of data data to be generated for each table
    -g <number> -t <table_index>        specify the number of lines of data data to be generated for given table. Table index can be found using -pto command
    -ar <requirement>                   adds requirement to the requirement list when engine is running. Prompts are used to customize the data generation output.
    -dr <number>                        deletes requirement from the requirement list when engine is running
    -pr                                 prints all saved requirements
    -q                                  quits the program
    -at                                 add table to prompt
    -dt                                 delete table from prompt
    -ct                                 clear tables added to prompt
    -st                                 see tables added to prompt
    -pp                                 print prompt
    --models                            see all models
    --setmodel <model_index>            set model
    --getmodel                          get current model

    """