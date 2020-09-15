from car import Car


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=70):
        """Initialize battery's attributes."""
        self.battery_size = battery_size

    def upgrade_battery(self, new_battery):
        self.battery_size = new_battery

    def describe_battery(self):
        """Print a statement describing the size of the battery."""
        print(f"This car has a {self.battery_size}-kwh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            car_range = 240
        elif self.battery_size == 85:
            car_range = 270

        message = f'This car can go for approximately {car_range} ' \
                  f'miles on a full charge.'
        print(message)

