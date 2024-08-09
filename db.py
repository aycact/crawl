import re
from clickhouse_driver import Client
# client = Client(host = 'localhost')
# def read_sql_file(file_path):
#     with open(file_path, 'r') as file:
#         return file.read()

# def parse_sql_commands(sql_content):
#     # Split the content into separate commands
#     # This simple approach assumes commands are separated by semicolons
#     commands = re.split(r';\s*', sql_content)
#     # Remove any empty commands
#     return [cmd.strip() for cmd in commands if cmd.strip()]

def execute_sql_commands(commands):
    client = Client('localhost')  # Replace with your ClickHouse server address
    
    # for command in commands:
    try:
        client.execute(*commands)
        print(f"Successfully executed: {commands}")
    except Exception as e:
        print(f"Error executing command: {commands}")
        print(f"Error message: {str(e)}")
# path = 'db.sql'
# content = read_sql_file(path)
# commands = parse_sql_commands(content)
commands = ('USE tuvi', 'USE default')
for command in commands:
    print(command)
execute_sql_commands(commands)
