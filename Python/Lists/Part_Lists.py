# A specific group in a list is called a slice

# Slicing a List
# To make a slice, you indicate the index of the first and last element you want to work with
print("\n")

players = [
    'benard', 'felix',
    'rashid', 'susan',
    'charles', 'alexander'
]
print(len(players))
print(players)
print(players[0:3])
print(players[:3])
print(players[3:])
print(players[-3:])
print('\n')

# Looping through a Slice
print("Here are the first three players on my team: ")
for player in players[:3]:
    print(player.title())
print("\n")


# Copying Lists
my_foods = ['pizza', 'biryani', 'chapati', 'rice', 'carrot cake']
friend_foods = my_foods[:]

print(f"My favorite foods are:\n\t {my_foods}")
print(f"My friend's foods are:\n\t {friend_foods}")
print("\n")

# Proving that we have two different lists
my_foods.append('mahamri')
friend_foods.append('fried chicken')
print(my_foods)
print(friend_foods)