# The Car Class
# We will write a new class representing a car.


class Car:
    """A simple attempt to model a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def descriptive_name(self):
        """Returns a neatly formatted descriptive name."""
        long_name = f"{self.year}, {self.make} {self.model}"
        return long_name.title()


my_new_car = Car('subaru', 's16', 2003)
print(my_new_car.descriptive_name())


