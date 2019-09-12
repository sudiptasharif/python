class Person(object):
    def __init__(self, fname, lname, dob, ssn):
        assert type(fname) == str and type(lname) == str and type(dob) == str and type(ssn) == str
        self.fname = fname
        self.lname = lname
        self.dob = dob
        self.ssn = ssn

    def __str__(self):
        return "(first_name = "+self.fname+", last_name = "+self.lname+", date_of_birth = "+self.dob+", ssn = "+self.ssn+")"


def hello():
    print("Yalo!")

print(type(hello))

sam = Person("samuel", "jackson", "1/1/1950", "123456789")
print(sam)

print(type(sam))
print(type(Person))

x = 2
print(type(x))

p = "name is blah"
print(type(p))

print(isinstance(sam, Person))


print(isinstance(x, str))

print(isinstance(x, int))


dave = Person(12, 12, 2, 3.25)
print(dave)
