##name = input("Please enter your name: ")
##print("Hello "+name+"!")


##height = input("How tall are you, in inches? ")
##height = int(height)
##
##if height >= 36:
##    print("\nYou are tall enough to ride!")
##else:
##    print("\nYou'll be able to ride when you're a little older.")

##msg = "Enter a number and I will tell you if it's odd or even: "
##number = input(msg)
##number = int(number)
##
##if number % 2 == 0:
##    print(number, "is even.")
##else:
##    print(number, "is odd.")

##msg = "How many people are in your dinner group: "
##number = int(input(msg))
##if number > 8:
##    print("You will have to wait for a table.")
##else:
##    print("Your table is ready.")

##msg = "Enter a number: "
##number = int(input(msg))
##
##if number % 10 == 0:
##    print(number, "is a multiple of 10.")
##else:
##    print(number, "is not a multiple of 10")        

##num = 1
##num_max = 10
##while num <= num_max:
##    print(num)
##    num += 1


prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
user_input = ""

while user_input != 'quit':
    user_input = input(prompt)
    if user_input != 'quit':
        print(user_input)
