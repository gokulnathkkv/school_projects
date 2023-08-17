import psycopg2

# Establish the database connection
connection = psycopg2.connect(
    dbname=,
    user=,
    password=,
    host=,
    port=,
)

cursor = connection.cursor()

try:
    # Input table name from the user
    table_name = input("Enter the table name: ")

    # Input column names and data types
    columns = []
    while True:
        column_name = input("Enter column name (or 'done' to finish): ")
        if column_name.lower() == 'done':
            break
        column_type = input(f"Enter data type for column '{column_name}': ")
        columns.append((column_name, column_type))

    # Construct the CREATE TABLE SQL statement
    create_table_query = f"CREATE TABLE {table_name} ({', '.join([f'{col[0]} {col[1]}' for col in columns])});"

    # Execute the CREATE TABLE query
    cursor.execute(create_table_query)
    connection.commit()
    print(f"Table '{table_name}' created successfully")

except Exception as e:
    print("Error:", e)
finally:
    if connection:
        connection.close()
