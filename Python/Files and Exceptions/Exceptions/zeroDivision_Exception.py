
print("Give me two numbers and I'll divide them for you.")
print("Key 'q' to quit.")

while True:
    first_number = input("\nEnter first Number: ")
    if first_number == 'q'.lower():
        break
    second_number = input("Enter second number: ")
    if second_number == 'q'.lower():
        break
    try:
        answer = float(first_number) / float(second_number)
    except ZeroDivisionError:
        print("You can't divide any number by zero!")
    else:
        print(answer)
