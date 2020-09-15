# Tuples are lists that cannot change
# The ability of not changing is referred to as immutability
# Parenthesis are used instead of square brackets
print("\n")

dimensions = (200, 50)
print(f"Width is {dimensions[1]} cm")
print(f"Height is {dimensions[0]} cm")
print(f"Area is:\n\t {dimensions[0] * dimensions[1]} sq cms")
print("\n")

# Although we can't modify the values, we can overwrite the values

dimensions = (200, 50)
print("Original dimensions: ")
for dimension in dimensions:
    print(dimension)
print("\n")

dimensions = (400, 100)
print("Modified dimensions: ")
for dimension in dimensions:
    print(dimension)
