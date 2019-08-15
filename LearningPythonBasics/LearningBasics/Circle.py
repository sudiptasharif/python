import math

class Circle(object):
    def __init__(self, radius):
        self.__radius = radius
        
    def setRadius(self, radius):
        self.__radius = radius
    
    def getRadius(self):
        return self.__radius
    
    def area(self):
        return math.pi * self.__radius ** 2
    
    def __add__(self, another_circle):
        return Circle(self.__radius + another_circle.__radius)
    
    def __sub__(self, another_circle):
        return Circle(self.__radius - another_circle.__radius)
    
    def __mul__(self, another_circle):
        return Circle(self.__radius * another_circle.__radius)
    
    def __lt__(self, another_circle):
        return self.__radius < another_circle.__radius
      
    def __le__(self, another_circle):
        return self.__radius <= another_circle.__radius
        
    def __eq__(self, another_circle):
        return self.__radius == another_circle.__radius
        
    def __ne__(self, another_circle):
        return self.__radius != another_circle.__radius
        
    def __gt_(self, another_circle):
        return self.__radius > another_circle.__radius
    
    def __ge__(self, another_circle):
        return self.__radius >= another_circle.__radius
    
    def __str__(self):
        return "Circle with radius "+str(self.__radius)
