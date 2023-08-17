import psycopg2

# Establish the database connection
connection = psycopg2.connect(
    dbname="Gokulnath",
    user="postgres",
    password="gokul",
    host="localhost",
    port="5432"
)
cursor = connection.cursor()

try:
    table_name = "class_management"

    # Create the table if it doesn't exist
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            id SERIAL PRIMARY KEY,
            total_classrooms INT,
            standard VARCHAR(255),
            section VARCHAR(255),
            max_students_per_class INT
        );
    """)
    connection.commit()
    print(f"Table '{table_name}' created")

    while True:
        print("Press 1 to insert class data")
        print("Press 2 to view class data")
        print("Press 3 to exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            total_classrooms = int(input("Enter total number of classrooms: "))

            for classroom_number in range(1, total_classrooms + 1):
                standard = input(f"Enter standard for classroom {classroom_number}: ")
                section = input(f"Enter section for classroom {classroom_number}: ")
                max_students = int(input(f"Enter max students for classroom {classroom_number} (<=40): "))

                if max_students <= 40:
                    insert_query = f"""
                        INSERT INTO {table_name} (total_classrooms, standard, section, max_students_per_class)
                        VALUES (%s, %s, %s, %s);
                    """
                    data_values = (total_classrooms, standard, section, max_students)

                    cursor.execute(insert_query, data_values)
                    connection.commit()
                    print(f"Data inserted for classroom {classroom_number}")
                else:
                    print("Maximum students per class should be 40 or less.")

        elif choice == '2':
            cursor.execute(f"SELECT * FROM {table_name};")
            rows = cursor.fetchall()

            if rows:
                for row in rows:
                    print(row)
            else:
                print("No class data to view")

        elif choice == '3':
            print("Exiting the program")
            break

        else:
            print("Invalid choice, please select again")

except Exception as e:
    print("Error:", e)
finally:
    if connection:
        connection.close()
