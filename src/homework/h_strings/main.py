import strings

def get_hamming_distance_or_dna_complement():
    exit_choice = False
    while not exit_choice:

        print("Welcome to Homework 5 menu, options:")
        print("1 - Hamming Distance")
        print("2 - DNA Complement")
        print("3 - Exit")

        menu_selection = int(input("Enter Selection: "))
    
        if menu_selection == 1:
            dna1 = input('Please enter DNA Sequence 1: ')
            dna2 = input('Please enter DNA Sequence 2: ')
            hamming_distance = strings.get_hamming_distance(dna1, dna2)
            print ('Hamming Distance: ' + str(hamming_distance))
        
        elif menu_selection ==2:
            dna = input('Please enter DNA Sequence: ')
            dna_complement = strings.get_dna_complement(dna)
            print ('Reverse Complement: ' + dna_complement)

        elif menu_selection == 3:
            print("Exiting Homework 5, have a great day!")
            exit_choice = True

        else:
            print("Sorry, that selection is invalid. Please select a number from 1 to 3.")

        if not exit_choice:
            exit_question = int(input("Enter 3 to exit now, or another number to return to the main menu: "))
            if exit_question == 3:
                exit_choice = True
    print("Thank you, come again!")

get_hamming_distance_or_dna_complement()