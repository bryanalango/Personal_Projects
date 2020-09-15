# A function is a block of codes designed to do one specific job

# Defining a Function


def greet_user():
    """Display a simple greeting."""
    print("Hello!")


greet_user()

print("\n")

# Passing Information to a Function


def greet_user(username):
    """Greets the user."""
    print(f"Hello, {username}!")


greet_user('Bryan')
greet_user('Sarah')
greet_user('Scott')


print("\n")

# Arguments and Parameters
# This is a piece of information the function needs to do its job.
# The variable username in the function greet_user() is an example of a parameter
# An argument is a piece of information that is passed from a function call to a function
# The value 'Bryan' in greet_user('Bryan') is an example of an argument

# Passing Arguments

# Positional Arguments


def describe_pet(animal_type, pet_name):
    """Displays information about a pet."""
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name}.")
    print("\n")


describe_pet('bunny', 'Rex')
describe_pet('cat', 'Willy')

print("\n")

# Keyword Arguments
# This is name-value pair that you pass to a function


def describe_pet(animal_type, pet_name):
    """Displays information about a pet."""
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name}.")
    print("\n")


describe_pet(animal_type='parrot', pet_name='Ray')
describe_pet(animal_type='squirrel', pet_name='Anne')

print("\n")

# Default Values


def describe_pet(pet_name, animal_type='dog'):
    """Displays information about a pet."""
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name}.")
    print("\n")


describe_pet(pet_name='Harry')
describe_pet('Rexy')


def describe_pet(pet_name = 'Gilly', animal_type='dog'):
    """Displays information about a pet."""
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name}.")


describe_pet()
describe_pet(animal_type='leopard', pet_name='Jaguar')
describe_pet('Charlie', 'cheetah')

# Styling Functions
# Functions should have descriptive names
# Function names should use lower case letters and underscores
# Module names should use the above conventions as well
# Every function should have a comment that explains what the function does
# The comment should appear immediately after the function definition
# Such comments should use docstring format
# If you specify default values in your parameters,
# no spaces should be used on either side of the equal sign
# The same convention should be used for key-word arguments
