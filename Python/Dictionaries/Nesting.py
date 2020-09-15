# Refers to storing lists in a dictionary or dictionaries in lists
# Dictionaries can also be stored inside dictionaries
print("\n")

# A list in Dictionaries

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_3 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_3]
for alien in aliens:
    print(alien)

# More Realistic Way
print("\n")

# Make 30 green aliens
aliens = []
for alien_number in range(30):
    new_alien = {
        'color': 'green', 'points': 5,
        'speed': 'slow', 'attack': 'lethal'
    }
    aliens.append(new_alien)

# Show first 5 Aliens
for alien in aliens[:5]:
    print(alien)

# Show how many aliens have been created
print("\n")
print(f"Total number of aliens: {len(aliens)}")

# Modifying the Aliens
print("\n")

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
        alien['attack'] = 'dangerous'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
        alien['attack'] = 'very dangerous'
for alien in aliens[0:5]:
    print(alien)

print("\n")
for alien in aliens:
    if alien['color'] == 'yellow':
        print(alien)
print("\n")

# A list in Dictionary
# Store information about a pizza being ordered
pizza = {
    'crust': 'thick',
    'toppings': ['mushroom', 'extra cheese'],
}

# Summarize the order
print(f"You ordered a {pizza['crust']}-pizza crust"
      f" with the following toppings: ")

for topping in pizza['toppings']:
    print(f"\t {topping}")

print("\n")
# Personal Practice Exercise
# Store a list of food being ordered
menu = {
    'beef stew': ['heavy', 'medium', 'light'],
    'addon': ['veges', 'salad', 'fruits' ],
    'drinks': ['latina', 'lemon juice', 'smoothie', 'crest'],
}

# Summarizing the order
print("Kindly receive your order as requested: ")
for addon in menu['addon']:
    print(f"\t {addon}")

print("\n")

# Favorite Languages

favorite_languages = {
    'bryan': ['python', 'sql'],
    'anne': ['javascript', 'html'],
    'samuel': ['c', 'c++'],
    'andrew': ['java'], 'gabriel': ['haskell'],
    'jackson': []
}

for name, languages in favorite_languages.items():
    print(f"{name.title()}'s favorite languages are: ")
    for language in languages:
        print(f"\t {language.title()}")
print("\n")

# Customizing it a bit
for user_name, fav_languages in favorite_languages.items():
    if len(fav_languages) == 1:
        print(f"{user_name.title()}'s favorite language is: ")
    elif len(fav_languages) > 1:
        print(f"{user_name.title()}'s favorite languages are: ")
    elif len(fav_languages) == 0:
        print(f"{user_name.title()} has no favorite language")

    for fav_language in fav_languages:
        print(f"\t {fav_language.title()}")

print("\n")

# Dictionary in a Dictionary

users = {
    'fidel': {
        'first_name': 'fidel',
        'last_name': 'ogono',
        'location' : 'migori',
    },
    'brian': {
        'first_name': 'brian',
        'last_name': 'wachira',
        'location': 'nakuru',
    },
    'anne': {
        'first_name': 'anne',
        'last_name': 'wariara',
        'location': 'nairobi'
    }
}

for username, user_info in users.items():
    print(f"Username: {username.title()}")
    full_name = user_info['first_name'] + " " + user_info['last_name']
    location = user_info['location']

    print(f"Full Name: {full_name.title()}")
    print(f"Location: {location.title()}")
    print("\n")

print("\n")

# Practice

players = dict(jackson={
    'first_name': 'jackson',
    'last_name': 'opiyo',
    'location': 'embakasi',
    'marital_status': 'married',
    'position': 'striker',
    'salary': 2000000
}, allan={
    'first_name': 'allan',
    'last_name': 'mwangi',
    'location': 'dandora',
    'marital_status': 'single',
    'position': 'goal keeper',
    'salary': 1500000
}, gilbert={
    'first_name': 'gilbert',
    'last_name': 'sultan',
    'location': 'kilimani',
    'marital_status': 'married',
    'position': 'defender',
    'salary': 800000
}, hassan={
    'first_name': 'hassan',
    'last_name': 'abdi',
    'location': 'peponi',
    'marital_status': 'single',
    'position': 'midfielder',
    'salary': 2500000
})

for jersey_name, player_info in players.items():
    print(f"Player Name: {jersey_name.title()}")
    player_name = player_info['first_name'] + " " + player_info['last_name']
    location = player_info['location']
    status = player_info['marital_status']
    position = player_info['position']
    salary = player_info['salary']

    print(f"Name on Jersey: {player_name.title()}")
    print(f"Position: {position.title()}")
    print(f"Salary: {salary}")
    print(f"Location: {location.title()}")
    print(f"Status: {status.title()}")
    print("\n")

