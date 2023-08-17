def get_section_names(num_sections):
    section_names = []
    for i in range(num_sections):
        section_name = input(f"Enter section name {i + 1}: ")
        section_names.append(section_name)
    return section_names


def view_sections(section_management):
    print("\nSection Management List:")
    for idx, section_names in enumerate(section_management, 1):
        print(f"{idx}. Sections: {', '.join(section_names)}")
        print()


def delete_sections(section_management):
    view_sections(section_management)
    choice = int(input("Enter the index of the sections to delete: "))
    if 1 <= choice <= len(section_management):
        del section_management[choice - 1]
        print("Sections deleted successfully.")
    else:
        print("Invalid index.")


def main():
    section_management = []

    while True:
        print("\nMenu:")
        print("1. Add Sections")
        print("2. View Sections")
        print("3. Delete Sections")
        print("4. Exit")

        choice = int(input("Enter your choice (1-4): "))

        if choice == 1:
            num_sections = int(input("Enter the number of sections: "))
            section_names = get_section_names(num_sections)
            section_management.append(section_names)
            print("Sections added successfully.")
        elif choice == 2:
            view_sections(section_management)
        elif choice == 3:
            delete_sections(section_management)
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
