def make_pizza(size, *toppings):
    """Summarizes the pizza we are about to make."""
    print(f"\nMaking {size}-inch pizza "
          f"with the following toppings:")
    for count, topping in enumerate(sorted(toppings), start=1):
        print(f"{count}. - {topping.title()}")
