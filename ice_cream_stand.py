from restaurant import Restaurant

class IceCreamStand(Restaurant):
    """Represents aspects of a restaurant, specific to ice cream stands"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes of the parent class."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla']

    def show_flavors(self):
        print("\nThe following flavors are available: ")
        for flavor in self.flavors:
            print("\t" + flavor)