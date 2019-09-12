class Fraction(object):
    """
    A number represented as a fraction
    """
    def __init__(self, num, denom):
        """
        :param num: integer numerator
        :param denom: integer denominator
        """
        assert type(num) == int and type(denom) == int, "ints not used"
        self.num = num
        self.denom = denom

    def __str__(self):
        """
        :return: Returns a string representation of self
        """
        return str(self.num) + "/" + str(self.denom)

    def __add__(self, other):
        """
        Adds two fractions
        :param other: other fraction
        :return: a new fraction representing the addition
        """
        top = self.num * other.denom + self.denom * other.num
        bottom = self.denom * other.denom
        return Fraction(top, bottom)

    def __sub__(self, other):
        """
        Subtracts two fractions
        :param other: other fraction
        :return: a new fraction representing the subtraction
        """
        top = self.num * other.denom - self.denom * other.num
        bottom = self.denom * other.denom
        return Fraction(top, bottom)

    def __float__(self):
        """
        returns the float value of the fraction
        :return: float value of fraction
        """
        return self.num / self.denom

    def __mul__(self, other):
        """
        multiplication of two fractions
        :param other: a Fraction object
        :return: a fraction that represents the multiplication
        """
        top = self.num * other.num
        bottom = self.denom * other.denom
        return Fraction(top, bottom)


a = Fraction(1, 4)
print(a)

b = Fraction(3, 4)
print(b)

c = a + b
print(c)

d = a - b
print(d)

print(float(c))
print(float(d))
