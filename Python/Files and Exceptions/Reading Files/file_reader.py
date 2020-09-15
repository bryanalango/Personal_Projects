# This we use the open() function
# The function needs only argument; The name id the file

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)

with open('Group_Scores.txt') as group_scores:
    output = group_scores.read()
    print(output.title().rstrip())  # .strip() removes the extra blank line after the output
print("\n")

# File Paths
# We have relative and absolute paths
# Relative paths are shorter
# Relatives paths are generally the same as where the python module is

# Absolute Paths

file_path = "C:/Users/BryanAlang'o/Desktop/Bee Class/Google_Meet_Link.txt"
with open(file_path) as file_object:
    content = file_object.read()
    print(content)
print("\n")

# Reading Line by Line

with open('Lorem_Ipsum.txt') as lorem:
    for line in lorem:
        print(line.rstrip())