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


my_new_car = Car('subaru', 's16', 2003)
print(my_new_car.descriptive_name())

my_new_car.update_odometer(30)
my_new_car.read_odometer()

print("\n")

my_old_car = Car('mercedes', 's-class', 2018)
print(my_old_car.descriptive_name())

my_old_car.update_odometer(250)
my_old_car.increment_odometer(180)
my_old_car.read_odometer()
