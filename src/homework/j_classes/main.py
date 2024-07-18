from class_a import Die

def roll_the_die():
    die = Die()
    while True:
        die.roll()
        print(f"You rolled a {die.get_rolled_value()}")
        roll_again = input("Roll again? (y/n): ")
        if roll_again != "y":
            break

roll_the_die()