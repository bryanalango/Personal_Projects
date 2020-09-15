# Modifying a List in a Function
# You you pass a list to a function, the function can modify the list
# Changes made to list inside the function are permanent

unprinted_designs = ['yokohama', 'adidas', 'nike', 'sony']
completed_designs = []

while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"{current_design.title()} is being printed.")
    completed_designs.append(current_design)


print("\nThe following designs have been printed:")
for completed_design in completed_designs:
    print(completed_design.title())
print("\n")

# Reorganizing the Above using Functions
# We will need two functions:
# 1) A function that will handle printing the designs
# 2) A function that will summarize the prints that have been been made


def print_models(unprinted_models, completed_models):
    """
    Simulate printing each design, until none is left.
    Move each design to a completed_models after printing.
    :return:
    """
    while unprinted_models:
        current_model = unprinted_models.pop()
        print(f"{current_model.title()} is being printed!")
        completed_models.append(current_model)


def show_completed_models(completed_models):
    """Show all the models that were printed"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model.title())


unprinted_models = ['yokohama', 'adidas', 'nike', 'sony']
completed_models = []

print_models(unprinted_models, completed_models)
show_completed_models(completed_models)
print(unprinted_models)
print("\n")

# Prevent a Function from Modifying a List
# This can be done by passing to the function a copy of the list
# Any changes the function makes to the list will only affect the copy
# You can send a copy of a list to a function like this:
#       function_name(list_name[:])

