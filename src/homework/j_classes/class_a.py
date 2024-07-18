from random import randint

class Die:

    def roll(self):
        self._roll_value = randint(1, 6)

    def get_rolled_value(self):
        return self._roll_value
    
    def __str__(self):
        return f"The rolled value is {self._roll_value}"