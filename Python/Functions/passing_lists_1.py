# Passing a List
# Say we have a list of users and we want to print a greeting to each

print("\n")


def greet_user(names):
    for name in names:
        message = f"Hello, {name.title()}!"
        print(message)


usernames = ['bryan', 'charles', 'simon']
greet_user(usernames)
print("\n")



