# Object-oriented programming is one of the most effective approaches of writing software
# You write classes that represent real-world things and situations
# Objects are created based on the classes
# A class defines the general behavior that the objects can have
# Instantiation is making an object from a class and you work with instances of a class
# An object is an instance of a class


class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name.title()} is snow sitting.")

    def roll_over(self):
        print(f"{self.name.title()} rolled over!")

    def show_age(self):
        print(f"{self.name.title()} is {self.age} years old.")


my_dog = Dog('ruby', 3)
my_dog.sit()
my_dog.roll_over()
my_dog.show_age()
print("\n")

print(f"My dog's name is {my_dog.name.title()}.\n"
      f"{my_dog.name.title()} is {my_dog.age} years old!")


your_dog = Dog('charlie', 2.5)
print(f"\nYour dog's name is {your_dog.name.title()}.\n"
      f"{your_dog.name.title()} is {your_dog.age} years old!")

print("\n")

your_dog.sit()
your_dog.roll_over()
your_dog.show_age()