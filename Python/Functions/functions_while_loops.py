def get_formatted_name(first_name, last_name):
    """Returns a full name, neatly formatted"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


user_name = get_formatted_name('Jim', 'Reeves')
print(user_name)
print("\n")


def get_formatted_name(first_name, last_name):
    """Returns a full name, neatly formatted"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


while True:
    f_name = input("Enter First Name: ")
    l_name = input("Enter Last Name: ")

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"Hello, {formatted_name.title()}!")
    break

print("\n")


def get_formatted_name(first_name, last_name):
    """Returns a full name, neatly formatted"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


while True:
    f_name = input("Enter First Name: ")
    print("Key in 'stop' to quit.")

    if f_name == 'stop':
        break

    l_name = input("Enter Last Name: ")
    if l_name == 'stop':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"Hello, {formatted_name.title()}!")
