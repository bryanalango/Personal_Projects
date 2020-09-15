# Writing to an Empty File

filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming in Python\n"
                      "And I also love swimming.\n")
print("\n")

# The various modes a file can be opened in include:
# r     - Read Mode
# w     - Write Mode
# a     - Append Mode
# r+    - Read and Write Mode

# If the mode is omitted, Python opens the file in read mode by default

with open('programming.txt', 'r') as new_file_object:
    lines = new_file_object.read()
    print(lines)




