"""
Dunder methods are magic methods in Python

They are used for representing a class
__str__, __repr__ 
"""

"""
__str__ => Converting Objects in a string
Represents an object to string when printed while keeping the  object as same
printing object will return the value under __str__.
"""

class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
    
    def __str__(self):
        return 'a {self.color} car'.format(self=self)

class CarNew:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
    
    # called when printing class using print
    def __str__(self):
        return '__str__ for class'
    
    # called when we are directly class name in the console for the purpose of inspecting
    def __repr__(self):
        return '__repr__ for class'

"""
__str__ => used to give an easy to read representation of your class, meant for human consumption
__repr__ => explicit view of what this object is.. Unambiguous view

"""

class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __repr__(self):
        return f'{self.__class__.__name__}({self.color}, {self.mileage})'

    def __str__(self):
        return f'My car color is: {self.color} and its mileage is: {self.mileage}!'


