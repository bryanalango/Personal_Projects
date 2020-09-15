# Stores data in the form of key-value pairs

alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

print("\n")

# Working with Dictionaries

student = {'name': 'bryan', 'age': 15, 'unit': 'Criminology'}
print(student)
print(student['name'].title())

print("\n")
new_point = alien_0['points']
print(f"You just earned {new_point} points!")

# Adding new Key_Value Pairs
# Dictionaries are immutable
print("\n")

print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
print("\n")

# Starting with an Empty Dictionary

alien_1 = {'color': 'red', 'points': 10}
print(alien_1, "\n")

# Modifying Values in a Dictionary

print(f"The alien color is {alien_0['color']}.")
alien_0['color'] = 'yellow'
print(f"The alien color is now {alien_0['color']}.")
print("\n")

# Move the alien to the right
# Determine how far to move based on its current speed
alien_0['speed'] = 'medium'
print(alien_0)
print(f"Original x-position: {alien_0['x_position']}")

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New x-position: {alien_0['x_position']}")
print("\n")

# Removing Key-Value Pairs
print(alien_0)
del alien_0['points']
print(alien_0)
print("\n")

# A Dictionary of Similar Objects
# class_register = dict()
# key = input("Enter key: ")
# value = input("Enter value: ")
# class_register[key] = value
# print(class_register)

print("\n")

# Practice on inserting items in a dictionary from users

# count = 1
# fav_colors = dict()
# limit = 2

# while count <= limit:
# name = input("Enter Name: ").title()
# fav_color = input("Enter favorite color: ").title()
# fav_colors[name] = fav_color
# count += 1
# print(fav_colors)

# print("\n")

favorite_languages ={
    'bryan': 'python',
    'samuel': 'java',
    'andrew': 'javascript',
    'roy': 'php',
    'james': 'pascal',
}

print(f"Bryan's favorite language is"
      f" {favorite_languages['bryan']}.")
