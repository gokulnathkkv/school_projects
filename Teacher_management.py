print("Enter number 1 to create Principal list")
print("Enter number 2 to Staff list")
print("Enter number 3 to visit principal list")
print("enter number 4 to visit staff list")
Principal_list = []
Staff_list = []
while True:
    Create_details = input("Enter your correct number:")
    if Create_details == "1":
        Principal_name = input("Enter principal name:")
        Experience = input("Enter principal experience:")
        Past_of_principal = input("Enter from old school name:")

        Leaving_reason = input("Enter reason for leaving Old school:")
        salary_expectations = input("Enter principal's salary expectations:")
        Contact_number = input("Enter principal mobile number:")
        Email = input("Enter principal email:")
        From = input("Enter your location:")
        Principal_collected_data = {
            "Principal_name": Principal_name,
            "Past_of_principal": Past_of_principal,
            "Experience": Experience,
            "Leaving_reason": Leaving_reason,
            "salary_expectations": salary_expectations,
            "Contact_number": Contact_number,
            "Email": Email,
            "From": From
        }
        change_files = Principal_list.append(Principal_collected_data)
        print("Your principal data", Principal_list)
    elif Create_details == "2":
        Staff_name = input('Enter staff name:')
        Age = input("Enter staff age:")
        Experience = input("Enter staff experience:")
        Past_of_staff = input("Enter from old school name:")
        Leaving_reason = input("Enter reason for leaving Old school:")
        salary_expectations = input("Enter staff salary expectations:")
        Contact_number = input("Enter staff mobile number:")
        Email = input("Enter staff email:")
        From = input("Enter your location:")
        Staff_collected_data = {
            "Staff_name": Staff_name,
            "Age": Age,
            "Experience": Experience,
            "Past_of_staff": Past_of_staff,
            "Leaving_reason": Leaving_reason,
            "salary_expectations": salary_expectations,
            "Contact_number": Contact_number,
            "Email": Email,
            "From": From
        }
        change_files = Staff_list.append(Staff_collected_data)
        print("Your principal data", Staff_collected_data)
    elif Create_details == "3":
        Name_principal = input("Enter principal name")
        for a in Principal_list:
            if a["Principal_name"] == Name_principal:
                print(a["Principal_name"])
                print(a["Past_of_principal"])
                print(a["Experience"])
                print(a["Leaving_reason"])
                print(a["salary_expectations"])
                print(a["Contact_number"])
                print(a["Email"])
                print(a["From"])
            else:
                print(Principal_list)
    elif Create_details == "4":
        Name_staff = input("Enter staff name")
        for b in Staff_list:
            if b["Staff_name"] == Name_staff:
                print(b["Staff_name"])
                print(b["Past_of_Staff"])
                print(b["Experience":])
                print(b["Leaving_reason"])
                print(b["salary_expectations"])
                print(b["Contact_number"])
                print(b["Email"])
                print(b["From"])
            else:
                print(Staff_list)
    else:
        print("Please enter valid number:")
#new changes in new code
