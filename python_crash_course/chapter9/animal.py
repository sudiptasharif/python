import random


class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def set_age(self, newage):
        self.age = newage

    def set_name(self, newname=""):
        self.name = newname

    def __str__(self):
        return "animal:"+str(self.name)+":"+str(self.age)


print("\n---- animal tests ---")
a = Animal(4)
print(a)
print(a.get_age())
a.set_name("fluffy")
print(a)
a.set_name()
print(a)

#################################
# Inheritance example
#################################


class Cat(Animal):

    def speak(self):
        print("meow")

    def __str__(self):
        return "cat:"+str(self.name)+":"+str(self.age)


print("\n--- cat tests ---")
c = Cat(5)
c.set_name("fluffy")
print(c)
c.speak()
print(c.get_age())
# a.speak()

#################################
# Inheritance example
#################################


class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)
        self.set_name(name)
        self.friends = []

    def get_friends(self):
        return self.friends

    def speak(self):
        print("hello")

    def add_friend(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)

    def age_diff(self, other):
        diff = self.age - other.age
        print(abs(diff), "years difference")

    def __str__(self):
        return "person:"+str(self.name)+":"+str(self.age)


print("\n--- person tests ---")
p1 = Person("jack", 30)
p2 = Person("jill", 25)
print(p1.get_name())
print(p1.get_age())
print(p2.get_name())
print(p2.get_age())
print(p1)
p1.speak()
p1.age_diff(p2)


#################################
# Inheritance example
#################################
class Student(Person):
    def __init__(self, name, age, major=None):
        Person.__init__(self, name, age)
        self.major = major

    def __str__(self):
        return "student:"+str(self.name)+":"+str(self.age)+":"+str(self.major)

    def change_major(self, major):
        self.major = major

    def speak(self):
        r = random.random()

        if r < 0.25:
            print("i have homework")
        elif 0.25 <= r <= 0.75:
            print("i need sleep")
        elif 0.5 <= r <= 0.75:
            print("i should eat")
        else:
            print("i am watching tv")
            

print("\n--- student tests ---")
s1 = Student("alice", 20, "CS")
s2 = Student("beth", 18)
print(s1)
print(s2)
s1.add_friend("john")
s1.add_friend("molly")
print(s1.get_friends())

print(s1.name)
print(s1.age)
print(s1.friends)

x = 23
y = 28
z = x + y




