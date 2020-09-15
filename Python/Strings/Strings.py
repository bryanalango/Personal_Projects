# A string is basically a character or a collection of characters
# Anything enclosed in a single or double quotes is a string

print("This is a string")
print('This is also a string')

# The use of both double and single quotes allows for flexibility

print("I told them that 'Python' is my language.")
print('Python, as many call it, is my "language."')

# Changing Cases in a String
name = "bryan da vinci"
print(name.title())
print(name.upper())

# A method is a function that Python can perform on a piece of data

print(name.lower())
print(name.upper())
print(name.islower())
print(name.isupper())
name_1 = name.upper()
print(name_1.isupper())
name_2 = name.title()
print(name_2)
print(name_2.istitle())


# Combining or Concatenating Strings
first_name = "Bryan"
last_name = "Otieno"
full_name = first_name + " " + last_name
print(full_name)

# Also, using F strings
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Dear {full_name.upper()}, welcome home!\n")

# Adding White Space to Strings with Tabs or Newlines
print("\tPython")
print("Preferred Languages:\n\tEnglish\n\tItalian\n\tElvish\n")

# Stripping White Space
fav_language = ' Python '
print(fav_language)
print(len(fav_language))

fav_language_1 = fav_language.rstrip().lstrip()
print(len(fav_language_1))
print(fav_language_1)
print("\n")


# Numbers in Python
integer = 2
decimal_or_float = 2.0
print(type(integer))
print(type(decimal_or_float))

# Operations for numbers that will give an 8
print(int(16/2))
print(int(4+4))
print(int(10 - 2))
print(4 * 2,"\n")

names = ["Bryan" ]
print("The game is over")