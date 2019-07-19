import enum


class Gender(enum.Enum):
    male = 1
    female = 2


class AleinType(enum.Enum):
    green = 1
    yellow = 2
    red = 3


class AlienColor(enum.Enum):
    green = 1
    yellow = 2
    red = 3


class AlienSpeed(enum.Enum):
    slow = 1
    medium = 2
    fast = 3


def describe_mugs(color, size, theme=""):
    if theme:
        print("I have a " + size + " mug, that's "+color + ". It has a " + theme + " theme.")
    else:
        print("I have a " + size + " mug, that's "+color + ".")


def describe_student(name, age, sex):
    if sex == Gender.female:
        pronoun = "She"
    elif sex == Gender.male:
        pronoun = "He"
    else:
        pronoun = name

    description = "Student's name is " + name.title() + ". " + pronoun + " is " + str(age) + " years old."
    print(description)


def get_alien_by_type(alien_type):
    if alien_type == AleinType.green:
        color = AlienColor.green
        point = 5
        speed = AlienSpeed.slow
    elif alien_type == AleinType.yellow:
        color = AlienColor.yellow
        point = 10
        speed = AlienSpeed.medium
    else:
        color = AlienColor.red
        point = 15
        speed = AlienSpeed.fast

    alien = {
        "color": color,
        "point": point,
        "speed": speed
    }
    return alien


def make_aliens(alien_type, number=1):
    aliens = []
    if number == 1:
        aliens.append(get_alien_by_type(alien_type))
    else:
        for counter in range(number):
            aliens.append(get_alien_by_type(alien_type))

    return aliens


def describle_book(author, book_name):
    print("The book "+book_name.title() + " is written by " + author.title() + ".")


"""Trying out the functions"""
# describe_mugs("red", "small", "christmas")
# describe_mugs("white", "large", "disney")
# describe_mugs("green", "large")
#
# describe_student("Sally", 19, Gender.female)
#
# # print(type(Gender.female))
# describe_student("John", 25, "garbage")
#
# describe_student("Megan", 21, 100)
#
# describe_student(sex=Gender.female, name="kelly", age=23)

print(make_aliens(AleinType.green, 3))
print(make_aliens(AleinType.red))
print(make_aliens(AleinType.yellow, 2))

describle_book(book_name="python crash course", author="eric matthes")
describle_book("j. k. rowling", "harry potter")


