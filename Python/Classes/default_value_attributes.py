class Car:
    """A simple attempt to model a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def descriptive_name(self):
        """Returns a neatly formatted descriptive name."""
        long_name = f"{self.year}, {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's reading!"""
        print(f"{self.make.title()} {self.model.title()} has {self.odometer_reading} miles on it!")


my_new_car = Car('subaru', 's16', 2003)
print(my_new_car.descriptive_name())
my_new_car.read_odometer()
