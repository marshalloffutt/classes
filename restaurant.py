# 9-1, 9-2, 9-4

class Restaurant():
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the name and cuisine attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.restaurant_name + " is a " + self.cuisine_type + " restaurant.")

    def open_restaurant(self):
        print(self.restaurant_name + " is now open for business.")

    def set_number_served(self, number):
        """
        Set the number served to the given value.
        Reject the change if it attempts to roll the number back.
        """
        if number >= self.number_served:
            self.number_served = number
        else:
            print("You can't roll back number served.")

    def increment_number_served(self, increment):
        """Add the given amount to the number served."""
        self.number_served += increment

    def show_number_served(self):
        print(str(self.number_served) + " served today.")

larrys_pizza = Restaurant("Larry's Pizza", "pizza")

larrys_pizza.open_restaurant()
larrys_pizza.describe_restaurant()

garys_burgers = Restaurant("Gary's Burgers", "burgers")
garys_burgers.describe_restaurant()

barrys = Restaurant("Barry's", "Chinese take-out")
barrys.describe_restaurant()

jerrys_chicken_hut = Restaurant("Jerry's Chicken Hut", "chicken tenders")
jerrys_chicken_hut.describe_restaurant()
jerrys_chicken_hut.set_number_served(3)
jerrys_chicken_hut.increment_number_served(4)
jerrys_chicken_hut.show_number_served()


