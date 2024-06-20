import repetition

def get_factorial_get_sum_odd_w_menu():
    exit_choice = False
    selection = 0
    while not exit_choice:

        print("Welcome to Homework 3 menu, options:")
        print("1 - Get Factorial")
        print("2 - Sum Odd Numbers")
        print("3 - Exit")

        menu_selection = int(input("Enter Selection: "))
    
        if menu_selection == 1:
            selection = 0
            while selection <= 0 or selection > 10:
                selection = int(input("Please enter a number <= 10 to get its factorial: "))
                if 0 < selection <=10:
                    print(repetition.get_factorial(selection))
                else:
                    print("Please enter a number from 1 to 10")
        
        elif menu_selection ==2:
            selection = 0
            while selection <= 0 or selection > 100:
                selection = int(input("Please enter a number <= 100 to get the sum of the odd numbers up to that number: "))
                if 0 < selection <=100:
                    print(repetition.sum_odd_numbers(selection))
                else:
                    print("Please enter a number from 1 to 100")

        elif menu_selection == 3:
            print("Exiting Homework 3, have a great day!")
            exit_choice = True

        else:
            print("Sorry, that selection is invalid. Please select a number from 1 to 3.")

        if not exit_choice:
            exit_question = int(input("Enter 3 to exit now, or another number to return to the main menu: "))
            if exit_question == 3:
                exit_choice = True
    print("Thank you, come again!")

get_factorial_get_sum_odd_w_menu()