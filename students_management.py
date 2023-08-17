import re

print("Create Student Details = 1")
print("View Student Details details = 2")
print("Delete Student Details = 3")
print("Edit Student Details = 4")
Students_data = []

while True:
    Condition = input("Enter your number:")

    if Condition == "1":
        Roll_no = input("Enter roll number: ")
        Name = input("Enter student name:")
        Age = input("Enter student age:")

        while True:
            Mobile_numbers = input("Enter student number:")
            # Phone number validation
            if re.match(r"^\d{10}$", Mobile_numbers):
                print("Phone number is valid.")
                break
            else:
                print("Invalid phone number. Please enter a 10-digit phone number.")

        while True:
            Emails = input("Enter student email:")
            # Email validation
            if re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", Emails):
                print("Email is valid.")
                break
            else:
                print("Invalid email address. Please enter a valid email.")

        Address = {
            "street": input("Enter street:"),
            "city": input("Enter city name:"),
            "district": input("Enter district name:"),
            "pincode": input("Enter pincode:")
        }

        collected_data = {
            "roll_Number": Roll_no,
            "Name": Name.capitalize(),
            "Age": Age,
            "Number": Mobile_numbers,
            "Emails": Emails,
            "Address": Address
        }
        Students_data.append(collected_data)
        print("Data is updated successfully")
        print("Current Students Data:", Students_data)

    elif Condition == "2":
        user_Roll_no = input("Enter roll number:")
        found = False
        for i in Students_data:
            if i["roll_Number"] == user_Roll_no:
                print(i["Name"])
                print(i["Age"])
                print(i["Number"])
                print(i["Emails"])
                print(i["Address"])
                found = True
                break
        if not found:
            print("Roll number is not defined")

    elif Condition == "3":
        user_Roll_no = input("Enter roll number:")
        for i in Students_data:
            if i["roll_Number"] == user_Roll_no:
                Students_data.remove(i)
                print("Data is updated successfully")
                print("Current Students Data:", Students_data)

    elif Condition == "4":
        Roll_no = input('Enter roll number:')
        for i in Students_data:
            if i["roll_Number"] == Roll_no:
                change_words = input("What detail do you want to change:")
                if change_words != "Address":
                    change_1 = input("Enter new changes:")
                    i[str(change_words)] = change_1
                    print("Your changes are successfully made.")
                    print("Current Students Data:", Students_data)
                elif change_words == "Address":
                    inside_Address = input("Address inside which detail do you want to change:")
                    change_1 = input("Enter new changes:")
                    i["Address"][str(inside_Address)] = change_1
                    print("Your changes are successful.")
                    print("Current Students Data:", Students_data)

    else:
        print("You have entered an invalid number. Please enter a valid number.")
