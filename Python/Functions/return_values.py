# Returning a Simple Value


def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


pianist = get_formatted_name('Jon', 'Snow')
print(pianist)

# Practice


def player_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()


man_u = player_name('david', 'de gea')
print(man_u)

# Making Arguments Optional
print("\n")


def get_formatted_name(first_name, middle_name, last_name):
    """Return a full name, neatly formatted"""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('Bryan', 'Otieno', last_name="Alang'o")
print(musician)
print("\n")

# But middle names aren't always needed


def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('Bryan', "Alang'o")
print(musician)
pianist = get_formatted_name(last_name='Orero', first_name='Scott')
print(pianist)
wizard = get_formatted_name('bryan', "Alang'o", middle_name='Otieno')
print(wizard)
print("\n")
