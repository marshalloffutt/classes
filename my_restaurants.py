from restaurant import Restaurant
from ice_cream_stand import IceCreamStand

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

harrys_ice = IceCreamStand("Harry's Ice", "ice cream")
harrys_ice.show_flavors()