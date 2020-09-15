# They are used to check conditions

print("\n")

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
print("\n")

# Conditional Tests
# An expression that can be evaluated as True or False

# Checking for Equality
car = 'audi'
if car == 'Audi':
    print(True)
else:
    print(False)

if car != 'Audi':
    print(True)
else:
    print(False)

print("\n")

# Checking Multiple Conditions
age_Bryan = 24
age_Anne = 23

if age_Anne > age_Bryan and age_Bryan < age_Anne:
    print("Lady is older")
else:
    print("Lady is younger")

print("\n")

if age_Anne >= age_Bryan or age_Bryan <= age_Anne:
    print("Lady is older")
else:
    print("Lady is younger")

# Checking whether a value is in a list or not
print("\n")

vegies = ['kales', 'spinach', 'tomatoes', 'cucumbers', 'cabbages']
print('kales' in vegies, "\n")

print('onions' not in vegies)

