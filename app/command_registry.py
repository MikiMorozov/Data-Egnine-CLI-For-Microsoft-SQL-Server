import app.command_exe as command_exe

engine_commands = {
    r'-w\s+.+)$': command_exe.write_data,
    '-idb': command_exe.insert_into_db,
    r'-g\s+\d+)$': command_exe.generate,
    r'-g\s+\d+)\s+-t\s+\d+)$': command_exe.generate_tables,
    r'-ar\s+.+)$': command_exe.add_requirement,
    r'-dr\s+\d+)$': command_exe.delete_requirement,
    '-pr': command_exe.print_requirements,
    r'-at\s+\d+)$': command_exe.add_table,
    r'-rt\s+\d+)$': command_exe.remove_table,
    '-st': command_exe.see_tables,
    '-pp': command_exe.print_prompt,
    '-ct': command_exe.clear_tables,
    }

non_engine_commands = { 
    '--help': command_exe.print_help,
    '-pt': command_exe.print_tables,
    '-ptr': command_exe.print_table_relationships,
    '-pto': command_exe.print_table_order,
    '--start': command_exe.start_engine, 
    '--stop': command_exe.stop_engine,
    '-q': command_exe.quit,
    '--models': command_exe.print_models, 
    r'--setmodel\s+\d+)$': command_exe.set_model,
    '--getmodel': command_exe.print_get_model,
    }