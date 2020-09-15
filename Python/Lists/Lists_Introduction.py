# A list is a collection of items in a particular order.
# Items in a list don't have to be related
# It's a good practice to make the name of your list plural.
# Square brackets [] indicate a list and items are separated by a comma

bicycles = ['trek', 'honda', 'cannonade','redline','specialized']
print(type(bicycles))
print(bicycles)

# Accessing Elements in  a list

print(bicycles[0])
print(bicycles[0], bicycles[1], bicycles[2])
print(f"""
1. {bicycles[0]}
2. {bicycles[1]}
3. {bicycles[2]}""")

print("\n")

print(bicycles[0].upper())

# Using Individual Values form a List

print("\n")
message = f"My first bicycle in the list is {bicycles[0].title()}."
print(message)
print("\n")

# Changing, Adding, and Removing Elements
# This is possible because Lists are Mutable(They can be modified)

# Modifying Elements in a List

motorcycles = ['Honda', 'Yamaha', 'Suzuki']
print(motorcycles)
motorcycles[2] = 'Ducati'
print(motorcycles, "\n")

# Adding Elements to a List
# Appending Elements to the End of the List

motorcycles.append('Ranger')
print(motorcycles, "\n")


# Inserting Elements into a List
# This adds elements to any position in the List
# You specify the index and the value of the new element

motorcycles.insert(2, 'Fergusson')
print(motorcycles, "\n")


# Removing Elements from a list
# Items are removed according to positions

del motorcycles[0]
print(motorcycles)
motorcycles.remove('Fergusson')
print(motorcycles)
motorcycles.index('Yamaha')
print(motorcycles)
print(motorcycles.index('Ranger'))
motorcycles[2] = 'Pajero'
print(motorcycles)
print('Pajero' in motorcycles)
print(motorcycles.index('Pajero'))
print("\n")

# Removing an Item Using pop() Method
# This removes the last Item in a List, but it let's use work with that item after removing it

print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
print("\n")

# Popping an Item from any Position in a list
print(motorcycles)
first_motorcycle = motorcycles.pop(0)
print(f"The first Motorcycle in the list is {first_motorcycle}")
print("\n")

# ORGANIZING A LIST
# Sorting a List Permanently
# We use the .sort() Method

cars = ['bmw', 'audi', 'nissan', 'toyota', 'subaru', 'mercedes']
cars.sort()
print(cars)

# Sorting the above list in a reverse alphabetical order
cars.sort(reverse=True)
print(cars)
print("\n")

# Sorting a List Temporarily
# We use the sorted() Function
cars_2 = ['toyota', 'lamborghini', 'audi', 'tesla']
print(f"Here is the original list:>> {cars_2}")
print(f"Here is the sorted list:>> {sorted(cars_2)}")
print(f"And here is the original list again:>> {cars_2}")
print("\n")

# The sorted() Function can also accept revers=True/False argument

print(sorted(cars_2, reverse=True), "\n")


# Printing a List in Reverse Order
animals = ['gladiator', 'lion', 'man', 'tiger', 'elephant']
print(animals.index('elephant'))
animals.reverse()
print(animals.index('elephant'))
print(animals, "\n")

# The reverse() method changes the order permanently and the same can revert the order

# Finding the Length of a List
print(animals)
print(len(animals))
print("\n")


# Avoiding Index Errors when Working with Lists

print(motorcycles)
motorcycles.append('honda')
motorcycles.append(popped_motorcycle)
print(motorcycles)

print(len(motorcycles))
print(motorcycles[-1])

# Printing the last item or the length of the list can help resolve such errors

# An intentional Error
print("\n")
televisions = ['Akira', 'Sony', 'LG', 'Mooka', 'Samsung']
print(len(televisions))
televisions.append('Telecast')
televisions.insert(2, 'TLC')
print(len(televisions))
print(televisions[-1], 'and', televisions[6])