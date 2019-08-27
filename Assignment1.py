"""
Replace the contents of this module docstring with your own details
Name: Davann Vuttha
Date started: 13 August 2019
GitHub URL:https://github.com/davannvuttha/Prog2_Assignment1
"""

csv_file = 'Places.csv'
file_location = open(csv_file, 'r')
places_list_n = file_location.readlines()
places_list = [i.replace("\n", '') for i in places_list_n]
file_location.close()
each_places_list = []
for i in range(len(places_list)):
    each_places_list.append(places_list[i].split(','))


def main():
    print("Welcome to Travel Tracker 1.0 - by Davann Vuttha")
    main_menu()
    exit("User quit program")


def main_menu():
    print("Menu: ")
    print("L - List places")
    print("A - Add places")
    print("M - Mark new place as visited")
    print("Q - Quit")
    print("")
    menu_input = input(">>>")
    print("")
    choices = ["l", "a", "m", "q"]
    menu_choice = menu_input.lower()
    while menu_choice not in choices:
        print("Invalid menu choices.")
        print("")
        menu_input = input(">>>")
        print("")
        menu_choice = menu_input.lower()
    while menu_choice != "q":
        if menu_choice == "l":
            print_places()
            main_menu()
        if menu_choice == "a":
            add_menu()
            main_menu()
        if menu_choice == "m":
            marked_menu()
            main_menu()

    write_file = open(csv_file, 'w')
    for j in range(len(each_places_list)):
        for i in range(4):
            write_file.write(str(each_places_list[j][i]) + ",")

        write_file.write("\n")
    write_file.close()
    print("{} places saved to {}".format(len(each_places_list), csv_file))
    print("Have a nice day :)")
    exit("")


def print_places():
    visit_count = 0
    for i in range(len(each_places_list)):
        if each_places_list[i][3] == "n":
            visit_count += 1
            print("*{}. {:<8} in {:<11} priority {}.".format(i + 1, each_places_list[i][0],
                                                             each_places_list[i][1],
                                                             each_places_list[i][2]))
        else:
            print(" {}. {:<8} in {:<11} priority {}.".format(i + 1, each_places_list[i][0],
                                                             each_places_list[i][1],
                                                             each_places_list[i][2]))
    print("")
    if visit_count > 0:
        print("you have visit {} places. You still want to visit {} places.".format(len(each_places_list), visit_count))
    else:
        print("you have visit {} places. No places left to visit. Why not add some more?".format(len(each_places_list)))
    print("")


def add_menu():
    add_name = input("Name: ")
    while add_name == "":
        print("Input cannot be blank.")
        add_name = input("Name: ")
    add_country = input("Country: ")
    while add_country == "":
        print("Input cannot be blank.")
        add_country = input("Country: ")
    add_priority = propriority_value("Please input a priority value: ")
    print("{} in {} (priority {}) added to Travel Tracker".format(add_name, add_country, add_priority))
    print("")
    new_place = [add_name, add_country, add_priority, "n"]
    each_places_list.append(new_place)


def propriority_value(message):
    number_value = int(input(message))
    while number_value <= 0:
        print("Number must be more than 0 ")
        number_value = int(input(message))
    return number_value


def marked_menu():
    print_places()
    none_visited_count = 0
    for i in range(len(each_places_list)):
        if each_places_list[i][3] == "n":
            none_visited_count += 1
    if none_visited_count == 0:
        print("No unvisited places.")
        print("")
        main_menu()
    print("Enter the number of the place to mark as visited.")
    ask_number = propriority_value(">>>")
    mark_number = ask_number - 1
    while mark_number > len(each_places_list):
        print("There aren't that many places.")
        print("Enter the number of the place to mark as visited.")
        ask_number = propriority_value(">>>")
        mark_number = ask_number - 1
    while each_places_list[mark_number][3] == "v":
        print("You have already visited that place.")
        print("Enter the number of the place to mark as visited.")
        ask_number = propriority_value(">>>")
        mark_number = ask_number - 1
    else:
        each_places_list[mark_number][3] = "v"
        print(
            "{} in {} visited.".format(each_places_list[mark_number][0], each_places_list[mark_number][1]))
        print("")


if __name__ == '__main__':

    main()
