# Introducing While Loops

# This loop runs as long as certain condition is true
print("\n")

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
print("\n")

# Letting user decide when to quit
prompt = "Tell me something and I'll repeat it to you."
prompt += "\nEnter 'quit' to end the program: "
message = ""

while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)

# Using a flag
print("\n")

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

print("\n")
# Practice

text = "Enter favorite number: "
text += "\nEnter '5' to terminate the program: "
status = True
message = ""

while status:
    message = int(input(text))
    if message == 5:
        status = False
    else:
        print(message)
print("\n")

# Using break to exit a Loop

prompt = "Enter name of the city you've visited."
prompt += "\n (Enter 'stop' when you are finished.) "

while True:
    city = input(prompt).title()

    if city == 'stop'.title():
        break
    else:
        print("You have visited: ")
print("\n")

# Using continue

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)
print("\n")

