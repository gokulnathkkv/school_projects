import psycopg2

connection = psycopg2.connect(

)

cursor = connection.cursor()
print("Database is connected successfully")

try:
    while True:
        print("Press 1 to view data from a table")
        print("Press 2 to exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            table_name = input("Enter the table name: ")

            try:
                cursor.execute(f"SELECT * FROM {table_name}")
                rows = cursor.fetchall()

                if rows:
                    headings = [desc[0] for desc in cursor.description]
                    print("Column names:", ', '.join(headings))
                    for row in rows:
                        print(', '.join(str(value) for value in row))
                else:
                    print("No data found in the table")

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
