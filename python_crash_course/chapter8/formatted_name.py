def get_formatted_name(first_name, last_name, middle_name=""):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()


# musician = get_formatted_name("jimi", "hendrix")
# print(musician)
#
# footballer = get_formatted_name("muhammad", "salah")
# print(footballer)
#
# footballer = get_formatted_name("lionel", "messi")
# print(footballer)
#
# musician = get_formatted_name("john", "lee", "hooker")
# print(musician)

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    first_name = input("First Name: ")
    if first_name == 'q':
        break

    last_name = input("Last Name: ")
    if last_name == 'q':
        break

    formatted_name = get_formatted_name(first_name, last_name)
    print("\nHello, "+formatted_name.title() + "!")




