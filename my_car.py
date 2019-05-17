from electric_car import ElectricCar

my_car = ElectricCar('toyota', 'prius', '2019')

print(my_car.get_descriptive_name())

my_car.odometer_reading = 23
my_car.read_odometer()

my_car.battery.describe_battery()
my_car.battery.upgrade_battery()
my_car.battery.describe_battery()