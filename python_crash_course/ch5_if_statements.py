cars = ["audi", "bmw", "subaru", "toyota"]

for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())


age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("You are not old enough to vote!")
    print("You don't have to vote")


club = "man city"

if club == "aresenal":
    print("It's not your favorite club.")
elif club == "man city":
    print("It's not your favorite club.")
    print("This club came won the EPL.")
elif club == "man united":
    print("The call themselves the red devil.")
    print("The are your clubs vicious rival.")
elif club == "liverpool":
    print("Yup that's your favorite club.")
else:
    print("This club is shit")






