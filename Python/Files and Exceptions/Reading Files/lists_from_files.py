file_name = 'pi_digits.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()
    print(lines)
    print(len(lines))
    print(type(lines))

print("\n")

for line in lines:
    print(line.rstrip())

print("\n")

# Replacing words in Strings

message = "I really like dogs."
print(message.replace('dogs', 'wolves'))