import dictionary

def get_dna_sequences():
    print("Please input a DNA sequence in list format, press enter, then input the next one. When you are finished input 'end' and press enter: ")
    dna_list = []
    while True:
        dna_input = input().strip()
        if dna_input.lower() == 'end':
            break
        
        if dna_input.startswith("[") and dna_input.endswith("]"):
            cleaned_input = dna_input[1:-1].replace(" ", "")
            dna_chars = cleaned_input.split(',')
            dna_chars = [char.strip("'") for char in dna_chars]
            dna_list.append(dna_chars)
        else:
            print("Invalid format. Please enter the DNA sequence in the format: ['A','T','G',...]")

    return dna_list

def get_p_distance_matrix_menu():
    exit_choice = False
    while not exit_choice:
        print("Welcome to Homework 6 menu, options:")
        print("1 - Get P Distance Matrix")
        print("2 - Exit")

        menu_selection = int(input("Enter Selection: "))
    
        if menu_selection == 1:
            dna_list = get_dna_sequences()
            p_distance_matrix = dictionary.get_p_distance_matrix(dna_list)
            print("[")
            for row in p_distance_matrix:
                
                row_str = ", ".join(f'{value:.1f}' for value in row)
                print(f' [{row_str}],')
            print("]")

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