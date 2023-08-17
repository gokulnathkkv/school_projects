import psycopg2

# Establish the database connection
connection = psycopg2.connect(

)

cursor = connection.cursor()

try:
    while True:
        print("Press 1 to delete a table")
        print("Press 2 to delete a column")
        print("Press 3 to delete a row")
        print("Press 4 to exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            # Delete a table
            table_to_delete = input("Enter the table name to delete: ")
            cursor.execute(f"DROP TABLE IF EXISTS {table_to_delete};")
            connection.commit()
            print(f"Table '{table_to_delete}' deleted successfully")

        elif choice == '2':
            # Delete a column
            table_name = input("Enter the table name: ")
            try:
                cursor.execute(f"SELECT * FROM {table_name} LIMIT 0")
                headings = [desc[0] for desc in cursor.description]
                print("Column names:", ', '.join(headings))
                column_to_delete = input("Enter column name to delete: ")
                if column_to_delete in headings:
                    alter_query = f"ALTER TABLE {table_name} DROP COLUMN {column_to_delete};"
                    cursor.execute(alter_query)
                    connection.commit()
                    print(f"Column '{column_to_delete}' deleted from '{table_name}' successfully")
                else:
                    print(f"Column '{column_to_delete}' does not exist in '{table_name}'")
            except psycopg2.ProgrammingError:
                print(f"Table '{table_name}' does not exist")

        elif choice == '3':
            # Delete a row
            table_name = input("Enter the table name: ")
            try:
                cursor.execute(f"SELECT * FROM {table_name} LIMIT 0")
                headings = [desc[0] for desc in cursor.description]
                print("Column names:", ', '.join(headings))
                column_to_match = input("Enter column name to match for row deletion: ")
                value_to_match = input(f"Enter value for '{column_to_match}' to match for row deletion: ")
                delete_query = f"DELETE FROM {table_name} WHERE {column_to_match} = %s;"
                cursor.execute(delete_query, (value_to_match,))
                connection.commit()
                print(f"Rows with '{column_to_match}' = '{value_to_match}' deleted from '{table_name}' successfully")
            except psycopg2.ProgrammingError:
                print(f"Table '{table_name}' does not exist")

        elif choice == '4':
            print("Exiting the program")
            break

        else:
            print("Invalid choice, please select again")

except Exception as e:
    print("Error:", e)
finally:
    if connection:
        connection.close()
