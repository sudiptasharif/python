# def describe_pet(animal_type, pet_name):
#     """Display information about a pet"""
#     print("\nI have a " + animal_type + ".")
#     print("My " + animal_type + "'s name is " + pet_name.title() + ".")


def describe_pet(pet_name, age=1, animal_type="dog"):
    """Display information about a pet"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
    print(pet_name.title() + " is " + str(age) + " years old.")


# # passing arguments to a function using positional arguments
# describe_pet('hamster', 'harry')
# describe_pet("dog", "willie")
#
# # passing arguments to a function using keyword arguments
# describe_pet(animal_type="horse", pet_name="shadow")
# describe_pet(animal_type="cat", pet_name="grumpy")

describe_pet("max")
describe_pet("lazy", animal_type="cat")
describe_pet("willie")

describe_pet(pet_name="long neck", animal_type="giraffe")
describe_pet("stripes", 10, "zebra")







