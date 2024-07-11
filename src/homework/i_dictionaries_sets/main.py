import dictionary

def get_p_distance_matrix_menu():
    exit_choice = False
    while not exit_choice:

        print("Welcome to Homework 6 menu, options:")
        print("1 - Get P Distance Matrix")
        print("2 - Exit")

        menu_selection = int(input("Enter Selection: "))
    
        if menu_selection == 1:
            dna1 = input('Please enter DNA List: ')
            p_distance = dictionary.get_p_distance_matrix(dna1)
            print ('P Distance: ' + p_distance)

        elif menu_selection == 2:
            print("Exiting Homework 6, have a great day!")
            exit_choice = True

        else:
            print("Sorry, that selection is invalid. Please select a number from 1 to 2.")

        if not exit_choice:
            exit_question = int(input("Enter 2 to exit now, or another number to return to the main menu: "))
            if exit_question == 2:
                exit_choice = True
    print("Thank you, come again!")

get_p_distance_matrix_menu()