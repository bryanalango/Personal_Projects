from car import Car

my_new_car = Car('audi', 's18', 2018)
print(my_new_car.descriptive_name())

my_new_car.odometer_reading = 25
my_new_car.increment_odometer(25)
my_new_car.read_odometer()


from car import ElectricCar

print("\n")

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()


# Importing Multiple Classes from a Module
print("\n")

from car import Car, ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2018)
print(my_tesla.descriptive_name())


# Importing an Entire Module
print("\n")


import car


my_tesla = car.Car('toyota', 'honda', 2019)
print(my_tesla.descriptive_name())

my_tesla = car.Car('tesla', 'legion', 2020)
print(my_tesla.descriptive_name())

