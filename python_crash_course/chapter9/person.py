import datetime


class Person:
    def __init__(self, name, surname, birthdate, address, telephone, email):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.address = address
        self.telephone = telephone
        self.email = email

    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year

        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1

        return age


person = Person("Jane", "Doe", datetime.date(1992, 1, 23), "1234 Test Street, Test City", "123 456 7891", "jane.doe@example.com")

print(person.name)
print(person.email)
print(person.age())
print(person.birthdate)
