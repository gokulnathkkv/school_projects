import psycopg2

connection = psycopg2.connect(

)

cursor = connection.cursor()
print("Database is connected successfully")

try:
    while True:
        print("Press 1 to create or insert into a table")
        print("Press 2 to exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            table_name = input("Enter the table name: ")

            try:
                cursor.execute(f"SELECT * FROM {table_name} LIMIT 0")
                headings = [desc[0] for desc in cursor.description]
                print("Column names:", ', '.join(headings))
                data_values = []
                placeholders = []

                for column_name in headings:
                    data_value = input(f"Enter value for '{column_name}': ")
                    data_values.append(data_value)
                    placeholders.append('%s')

                formatted_column_names = ', '.join(['"' + col + '"' for col in headings])
                formatted_placeholders = ', '.join(placeholders)

                insert_query = f'INSERT INTO {table_name} ({formatted_column_names}) VALUES ({formatted_placeholders});'

                cursor.execute(insert_query, data_values)
                connection.commit()
                print("Data inserted successfully")
            except psycopg2.ProgrammingError:
                print("Table does not exist")

        elif choice == '2':
            print("Exiting the program")
            break

        else:
            print("Invalid choice, please select again")

except Exception as e:
    print("Error:", e)
finally:
    if connection:
        connection.close()
