# Moving Items from One List to Another

# Start with users that need to be verified
# Create an Empty list to hold confirmed users

unconfirmed_users = ['bryan', 'anne', 'alex', 'joyce']
confirmed_users = []

while unconfirmed_users:
    current_users = unconfirmed_users.pop()

    print(f"Verifying user: {current_users.title()}")
    confirmed_users.append(current_users)
print("\n")

print(f"The following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

print("\n")
# Practice

unconfirmed_usernames = ['john', 'kelly', 'kith', 'rhody']
confirmed_usernames = []

while unconfirmed_usernames:
    current_usernames = unconfirmed_usernames.pop()
    print(f"The following username is being confirmed:"
          f" {current_usernames.title()}")

    confirmed_usernames.append(current_usernames)
print("\n")

print("The following usernames have been confirmed: ")
for count, confirmed_username in enumerate(sorted(confirmed_usernames),start=1):
    print(f"{count}. {confirmed_username.title()}")
print("\n")

# Removing all Instances of an Item in a List
pets = ['dog', 'cat', 'parrot', 'cat', 'bunny', 'cat', 'goldfish', 'dog']
print(pets)

while 'cat' and 'dog' in pets:
    pets.remove('cat')
    pets.remove('dog')

print("\n")

# Filling in a Dictionary with User Input
responses = dict()
polling_active = True

while polling_active:
    name = input("Enter Name: ").lower()
    fav_mountain = input("What's your favorite Mountain: ").lower()

    responses[name] = fav_mountain

    repeat = input("Would you like another person to take the poll? (yes/no) ").lower()
    if repeat == 'no':
        polling_active = False
print("\n")

print(".......Polling Results......")
for name, response in sorted(responses.items()):
    print(f"{name.title()} would like to climb Mt {response.title()}")