print("enter number 1 to create information")
print("enter number 2 to visit list`")
School_data = []
while True:
    Create_information = input("Enter correct number to create information:")
    if Create_information=="1":
        School_name = input("Enter your school name:")
        Founder_name = input("Enter school founder name:")
        School_stating_year = input("Enter school starting year:")
        School_type = input("How many standards in our school:___ to ___:")
        Education_type = input("Your school CBSC or Matric please enter here:")
        Contact = input("Enter our school official contact number:")
        Email = input("Enter our school official email:")
        Website = input("Enter our school online website:")
        Location = input("Enter our school location:")
        collected_information={
            "School_name":School_name,
            "Founder_name":Founder_name,
            "School_stating_year":School_stating_year,
            "School_type":School_type,
            "Education_type":Education_type,
            "Contact":Contact,
            "Email":Email,
            "Website":Website,
            "Location":Location
        }
        File_shift=School_data.append(collected_information)
        print("Your new updated data:",collected_information)
        print('Your old datas:',File_shift)
    elif Create_information=="2":
        for a in School_data:
            print(a)
    else:
        print('Enter correct number:')