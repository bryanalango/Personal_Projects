filename = 'alice.txt'

try:
    with open(filename) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    message = f"Sorry, the file '{filename}' does not exist."
    print(message)

print("\n")

title = "Alice in Wonderland"
print(title.split())