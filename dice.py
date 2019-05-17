from random import randint

class Die():
    def __init__(self, number_of_sides=6):
        self.number_of_sides = number_of_sides

    def roll_die(self):
        roll = randint(1, self.number_of_sides)
        print('You rolled a ' + str(roll))