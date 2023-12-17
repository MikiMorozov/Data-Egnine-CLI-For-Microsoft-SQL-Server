import command_exe as command_exe

engine_commands = {
    r'-w\s+(.+)$': command_exe.write_data,
    r'\s*-idb\s*': command_exe.insert_into_db,
    r'-g\s+(\d+)$': command_exe.generate,
    r'-g\s+(\d+)\s+-t\s+(\d+)$': command_exe.generate,
    r'-ar\s+(.+)$': command_exe.add_requirement,
    r'-dr\s+(\d+)$': command_exe.delete_requirement,
    r'\s*-pr\s*': command_exe.print_requirements,
    r'-at\s+(\d+)$': command_exe.add_table,
    r'-dt\s+(\d+)$': command_exe.delete_table,
    r'\s*-st\s*': command_exe.see_tables,
    r'\s*-pp\s*': command_exe.print_prompt,
    r'\s*-ct\s*': command_exe.clear_tables,
    }

non_engine_commands = { 
    r'\s*--help\s*': command_exe.print_help,
    r'^\-pt$': command_exe.print_tables,
    r'\s*-ptr\s*': command_exe.print_table_relationships,
    r'\s*-pto\s*': command_exe.print_table_order,
    r'\s*--start\s*': command_exe.start_engine, 
    r'\s*--stop\s*': command_exe.stop_engine,
    r'\s*-q\s*': command_exe.quit,
    r'\s*--models\s*': command_exe.print_models, 
    r'--setmodel\s+(\d+)$': command_exe.set_model,
    r'\s*--getmodel\s*': command_exe.print_get_model,
    }