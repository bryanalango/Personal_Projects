# Looping through all Key-Value Pairs
print("\n")

user_0 = {
    'username': 'b.otieno',
    'first_name': 'bryan',
    'last_name': 'otieno',
}

for key, value in user_0.items():
    print(f"Key: {key}")
    print(f"Value: {value}", "\n")
print("\n")

# Favorite Languages
favorite_languages = {
    'bryan': 'python',
    'anne': 'javascript',
    'samuel': 'java',
    'andrew': 'swift',
}
for name, language in favorite_languages.items():
    print(f"{name.title()} loves {language.title()}.")

print("\n")

# Looping Through all Keys
# The keys() method if useful here
print(favorite_languages, "\n")
for count, name in enumerate(favorite_languages.keys(), start = 1):
    print(f"{count}. {name.title()}")
print("\n")

for count, name in enumerate(favorite_languages, start = 1):
    print(f"{count}. {name.title()}")
print("\n")

friends = ['bryan', 'alex', 'andrew', 'simon', 'anne']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print(f"Hi {name.title()}, "
              f"I can see you love {favorite_languages[name].title()}!")

print("\n")

# Checking if an item in a list is not in a dictionary
for name in friends:
    if name not in favorite_languages.keys():
        print(f"{name.title()}, kindly take our poll!")

print("\n")

# Looping Through a Dictionary's Keys in Order

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking our poll.")

print("\n")

# Looping through all values in Dictionary
# The values() is helpful here

print("The following languages have been mentioned "
      "in alphabetical order:")
for count, languages in enumerate(sorted(favorite_languages.values()), start=1):
    print(f"{count}. {languages.title()}")
print("\n")

favorite_languages['michael'] = 'python'
favorite_languages['richard'] = 'java'
print(favorite_languages)

print("\n")


# Checking for Duplicates
values_in_favs = list(favorite_languages.values())
print(f"Keys are: \n\t{favorite_languages.keys()}")
print(f"Values are: \n\t{favorite_languages.values()}")

unique_keys = set(favorite_languages.keys())
unique_values = set(favorite_languages.values())
print(f"Unique Keys are:\n\t {unique_keys}")
print(f"Unique values are:\n\t {unique_values}")

print("\n")
for unique in unique_values:
    if unique in favorite_languages.values():
        if values_in_favs.count(unique) == 1:
            print(f"{unique} appears {values_in_favs.count(unique)} time")
        else:
            print(f"{unique.title()} appears {values_in_favs.count(unique)} times")
