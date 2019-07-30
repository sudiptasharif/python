def make_car(manufacturer, model, **info):
    """Stores information about a car in a dictionary and return that dictionary"""
    car = {}
    car["manufacturer"] = manufacturer
    car["model"] = model

    for key, value in info.items():
        car[key] = value

    return car

subaru = make_car("subaru", "outback", color="blue", tow_package=True)
toyota = make_car("toyota", "camry", color="red", tow_package=False, gear="automatic", engine="four cylander")

print(subaru)
print(toyota)
