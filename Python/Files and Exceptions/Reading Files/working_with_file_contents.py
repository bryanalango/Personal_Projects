# After you've read a file into memory, you can manipulate the file.

file_name = 'pi_digits.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()

pi_string= ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))
print("\n")

file_name = 'pi_digits.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()

pi_string= ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))


