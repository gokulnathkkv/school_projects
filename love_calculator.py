def calculate_love_percentage(name1, name2):
    combined_names = name1.lower() + name2.lower()
    love_count = 0

    for char in "truelove":
        love_count += combined_names.count(char)

    love_percentage = love_count * 10
    return love_percentage


def main():
    print("Welcome to the Love Calculator!")
    name1 = input("Enter the first name: ")
    name2 = input("Enter the second name: ")

    love_percentage = calculate_love_percentage(name1, name2)

    print(f"\nLove Percentage between {name1} and {name2} is: {love_percentage}%")


if __name__ == "__main__":
    main()
