# The original class is called the parent class
# The new class is called the child class
# The child class inherits every attribute and method from its parent class
# The child class is also free to define new attributes and methods of its own

# The __init__() Method for a Child Class


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


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.descriptive_name())

my_tesla.update_odometer(300)
my_tesla.read_odometer()

my_tesla.increment_odometer(150)
my_tesla.read_odometer()