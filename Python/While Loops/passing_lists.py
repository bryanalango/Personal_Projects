def greet_users(names):
    """Print a simple greeting to each user in the list"""
    for name in names:
        message = f"Hello, {name.title()}"
        print(message)


usernames = ['bryan', 'babra', 'anne', 'benedict', 'rogers', 'simon', 'gilly']
greet_users(sorted(usernames))

print("\n")

# Trying it with a dictionary


def countries_info(countries):
    """Prints a simple info about a country"""
    for country, info in countries.items():
        output = f"{country.title()} is known for {info.title()}."
        print(output)


countries_wiki = {
    'kenya': 'tourism',
    'uganda': 'wildlife',
    'nigeria': 'oil',
    'south africa': 'diamond',
}

countries_info(countries_wiki)

print("\n")

# Modifying a List in a Function

# Without using a Function

# Starting with some designs that need to be printed
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron', 'posters']
completed_models = []

# Simulate printing each design, until none is left
# Move each design to completed_models after printing
while unprinted_designs:
    current_design = unprinted_designs.pop()

    # Simulate creating a 3D print from the design
    print(f"Printing model: {current_design.title()}")
    completed_models.append(current_design)

# Display all Models
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model.title())
print()

# The above code can be organized using two functions


def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design until none is left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        print(f"Printing Model: {current_design.title()}")
        completed_models.append(current_design)


def show_completed(completed_models):
    """Show all the models that were printed"""
    print("\nThe following models were printed:")
    for completed_model in completed_models:
        print(completed_model.title())


unprinted_designs = ['yokohama', 'adidas', 'nike']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed(completed_models)

print("\n")

# Practice


def user_database(unconfirmed_users, confirmed_users):
    while unconfirmed_users:
        current_users = unconfirmed_users.pop()
        print(f"{current_users.title()} is being confirmed.")
        confirmed_users.append(current_users)


def show_confirmed(confirmed_usernames):
    print(f"\nThe following users have been confirmed:")
    for confirmed_username in confirmed_usernames:
        print(confirmed_username.title())


unconfirmed_users = ['aisha', 'james', 'gilbert', 'maryam', 'anne']
confirmed_users = []

user_database(unconfirmed_users, confirmed_users)
show_confirmed(confirmed_users)
print("\n")

# Preventing a Function from Modifying a List
