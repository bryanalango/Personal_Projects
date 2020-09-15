class Car:
    """A simple attempt to model a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 25

    def descriptive_name(self):
        """Returns a neatly formatted descriptive name."""
        long_name = f"{self.year}, {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's reading!"""
        print(f"{self.make.title()} {self.model.title()} has {self.odometer_reading} miles on it!")

    def update_odometer(self, mileage):
        """Set the odometer reading to a given value."""
        self.odometer_reading = mileage

        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

        # Incrementing an Attribute's value through a Method

    def increment_odometer(self, miles):
        self.odometer_reading += miles


# Inheritance begins here


class ElectricCar(Car):
    """Represents aspects of a car specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes if the parent class."""
        super().__init__(make, model, year)
        self.battery_size = 70

    # Defining Attributes and Methods for the Child Class

    def describe_battery(self):
        """Print a statement describing the size of the battery."""
        print(f"{self.make.title()} {self.model.title()} has a "
              f"{self.battery_size}-kwh battery.")

    # Overriding Methods from the Parent Class

    def fill_gas_tank(self):
        """Electric Cars don't have gas tanks."""
        print(f"{self.make.title()} {self.model.title()} doesn't "
              f"need a gas tank!")


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.descriptive_name())

my_tesla.describe_battery()
my_tesla.fill_gas_tank()