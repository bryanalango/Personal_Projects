def make_pizza(*toppings):
    """Prints the list of toppings that have been requested"""
    print(toppings)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
print("\n")


# Looping through the list


def make_pizza(*toppings):
    print("\nMaking pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping.title()}")


make_pizza('peperoni')
make_pizza('coriander', 'mushrooms')
print("\n")


# Mixing Positional and Arbitrary Arguments


def make_pizza(size, *toppings):
    print(f"\nMaking a {size}-inch pizza"
          f" with the following toppings:")
    for count, topping in enumerate(sorted(toppings), start=1):
        print(f"{count}. - {topping.title()}")


make_pizza(12, 'peperoni')
make_pizza(14, 'lavender', 'mushrooms', 'extra cheese')
print("\n")


# Using Arbitrary Keyword Arguments


def build_profile(first_name, last_name, **user_info):
    """Builds a dictionary containing everything we know about a user"""
    profile = dict()
    profile['first_name'] = first_name
    profile['last_name'] = last_name
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)
print("\n")


# Practice


def user_data(first_name, last_name, **info):
    profile = dict()
    profile['first_name'] = first_name
    profile['last_name'] = last_name
    for data, data_info in info.items():
        profile[data] = data_info
    return profile


user_1 = user_data('bryan'.title(), 'otieno'.title(),
                   status='single'.title(),
                   location='Nairobi'.title(),
                   education='university'.title(),
                   pets='wolves'.title())

print(user_1)

print("\nThis is the summary of the above info:")
for info, details in user_1.items():
    print(f"{info.title()}: {details.title()}")
