def make_sandwiches(*items):
    """Prints a summary of the sandwich that is being ordered."""
    print("\nMaking a sandwich with the following items:")
    for item in items:
        print("- " + item)

make_sandwiches("chicken", "onions", "mushrooms", "tomato")
make_sandwiches("chicken", "onions")
make_sandwiches("beef", "mushrooms")

