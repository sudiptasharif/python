##cars = ["audi", "bmw", "subaru", "toyota"]
##
##for car in cars:
##    if car == "bmw":
##        print(car.upper())
##    else:
##        print(car.title())
##
##
##age = 19
##if age >= 18:
##    print("You are old enough to vote!")
##    print("Have you registered to vote yet?")
##else:
##    print("You are not old enough to vote!")
##    print("You don't have to vote")
##
##
##club = "man city"
##
##if club == "aresenal":
##    print("It's not your favorite club.")
##elif club == "man city":
##    print("It's not your favorite club.")
##    print("This club came won the EPL.")
##elif club == "man united":
##    print("The call themselves the red devil.")
##    print("The are your clubs vicious rival.")
##elif club == "liverpool":
##    print("Yup that's your favorite club.")
##else:
##    print("This club is shit")
##
##
##
##print("Hello Geany")
##
##channel = "bbcw"
##
##if(channel == "itv"):
##    print("The channel is itv")
##    print("One of my favorite tv shows is in itv: midsomer murders")
##elif(channel == "bbc"):
##    print("bbc always has good shows")
##    print("it's the worlds oldest broadcasting network")
##elif(channel == "cnn"):
##    print("this channel is american")
##    print("i don't like it as much, as they seem fake and just full of sound bits")
##else:
##    print("are you talking about an adut chaneel mate? piss off.")
##    print("idiot")
##
##nums = [2, 4, 5, 6, 8]
##num = 12
###print(msg)
##
##adjective = "beauty"
##
##if(num in nums):
##    msg = ":You found a number in the list. you are a genious you "+adjective
##    print(num, msg)
##else:
##    msg = ":That's not a number in the list, you "+adjective
##    print(num, msg)
##
##
##subjects = ["english", "physics", "chemistry", "biology", "math", "computer science"]
##subject = "sports education"
##
##if(subject in subjects):
##    print("My fav subject is in my list")
##    print("I am very glad that it is")
##else:
##    print("Why is "+subject+" not in my list? It's fucked up. I  love "+subject)
##    print("All i want to is lear about "+subject)
##
##colors = []
##colors.append("red")
##colors.append("green")
##colors.append("blue")
##colors.append("yellow")
##colors.append("orange")
##
##color = "olive"
##
##if(color not in colors):
##    print(color, " is not is the list: ", colors)
##    print("I don't know why it's missing")
##else:
##    print(color, " is in  the list. I don't beleive it.")
##    print("it's amazing")

age = 25

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5

print("Your admission cost is $"+str(price)+".")

requested_toppings = ["mushrooms", "extra cheese", "pineapple"]

if "mushrooms" in requested_toppings:
    print("adding mushrooms")
if "chicken" in requested_toppings:
    print("adding chicken")
if "beef" in requested_toppings:
    print("adding beef")
if "pineapple" in requested_toppings:
    print("adding pineapple")
if "extra cheese" in requested_toppings:
    print("adding extra cheese")

print("\nFinished making your pizza")























