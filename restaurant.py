# 9-1, 9-2

class Restaurant():
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the name and cuisine attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name + " is a " + self.cuisine_type + " restaurant.")

    def open_restaurant(self):
        print(self.restaurant_name + " is now open for business.")

larrys_pizza = Restaurant("Larry's Pizza", "pizza")

larrys_pizza.open_restaurant()
larrys_pizza.describe_restaurant()

garys_burgers = Restaurant("Gary's Burgers", "burgers")
garys_burgers.describe_restaurant()

barrys = Restaurant("Barry's", "Chinese take-out")
barrys.describe_restaurant()

jerrys_chicken_hut = Restaurant("Jerry's Chicken Hut", "chicken tenders")
jerrys_chicken_hut.describe_restaurant()


