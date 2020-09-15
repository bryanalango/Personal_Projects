import collections
fav_languages = collections.OrderedDict()

favorite_languages = {
    'bryan': 'python',
    'anne': 'javascript',
    'samuel': 'java',
    'andrew': 'swift',
}
for name, language in favorite_languages.items():
    print(f"{name.title()} loves {language.title()}")

print("\n")
fav_languages['jen'] = 'python'
fav_languages['sarah'] = 'java'
fav_languages['bryan'] = 'c'
fav_languages['anne'] = 'python'

for name, language in fav_languages.items():
    print(f"{name.title()}'s favorite language "
          f"is {language.title()}")
