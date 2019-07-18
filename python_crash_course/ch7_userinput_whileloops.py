# name = input("Please enter your name: ")
# print("Hello "+name+"!")
#
#
# height = input("How tall are you, in inches? ")
# height = int(height)
#
# if height >= 36:
#    print("\nYou are tall enough to ride!")
# else:
#    print("\nYou'll be able to ride when you're a little older.")
#
# msg = "Enter a number and I will tell you if it's odd or even: "
# number = input(msg)
# number = int(number)
#
# if number % 2 == 0:
#    print(number, "is even.")
# else:
#    print(number, "is odd.")
#
# msg = "How many people are in your dinner group: "
# number = int(input(msg))
# if number > 8:
#    print("You will have to wait for a table.")
# else:
#    print("Your table is ready.")
#
# msg = "Enter a number: "
# number = int(input(msg))
#
# if number % 10 == 0:
#    print(number, "is a multiple of 10.")
# else:
#    print(number, "is not a multiple of 10")
#
# num = 1
# num_max = 10
# while num <= num_max:
#    print(num)
#    num += 1
#
#
# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "
# user_input = ""
#
# while user_input != 'quit':
#    user_input = input(prompt)
#    if user_input != 'quit':
#        print(user_input)
#
#
# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "
#
# active = True
#
# while active:
#    msg = input(prompt)
#
#    if msg == 'quit':
#        active = False
#    else:
#        print(msg)
#
#
#
# prmt = "\nPlease enter the name of a city you have visited: "
# prmt += "\n(Enter 'quit' when you are finished.) "
#
# while True:
#    city = input(prmt)
#
#    if city == 'quit':
#        break
#    else:
#        print("I'd love to go to " + city.title() + "!")
#
# print("Thank you for your input.")
#
#
# curr_num = 0
#
# while curr_num < 10:
#    curr_num += 1
#    if curr_num % 2 == 0:
#        continue
#    print(curr_num)

# unconfirmed_users = ["alice", "brian", "candace"]
# confirmed_users = []
#
# while unconfirmed_users:
#     confirmed_user = unconfirmed_users.pop()
#
#     print("Verifying user: "+confirmed_user.title())
#     confirmed_users.append(confirmed_user)
#
# print("\nThe following users have been confirmed: ")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())

# pets = ["dog", "cat", "dog", "goldfish", "cat", "rabbit", "cat"]
# print(pets)
#
# while "cat" in pets:
#     pets.remove("cat")
#
# print(pets)

responses = {}

# Set a flag to indicate that polling is active
polling_active = True

while polling_active:
    # prompt for the person's name and response
    name = input("\nWhat's your name? ")
    response = input("Which city would you like to visit? ")

    # store the response in the dictionary
    responses[name] = response

    # find out if anyone else is going to take the poll
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == "no":
        polling_active = False


# polling is complete show the result:
print("\n--- Polling Results ---")
for name, response in responses.items():
    print(name.title() + " would like to visit "+response.title() + ".")





