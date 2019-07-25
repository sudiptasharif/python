# def greet_user(username):
#     """Display a simple greeting."""
#     print("Hello, " + username.title())
#
#
# greet_user("sudipta")
# greet_user("silvia")
# greet_user("ridwan")
#
# greet_user()


def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)


usernames = ["hannah", "ty", "margot"]
greet_users(usernames)
