"""
Use of Super Keyword in Python
"""
"""
This example is exactly not the best because it violates the LSP but for demonstration purposes it can be used
"""

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width
    
    def what_am_i(self):
        return 'Rectangle'
    
    def what_am_i(self):
        return 'Square'

class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

class Cube(Square):
    def surface_area(self):
        # Python will first look for the area method in Cube class
        # IF it does not find an area method in the cube class then
        # It will move to its parent class the is square
        face_area = self.area()
        return face_area * 6

    def volume(self):
        # Python will directly look for the area method in the
        # parent class
        # Inheritance chain =>  Cube->Square->Rectangle->Object
        # Class.__mro__ => Shows the inheritance chain
        face_area = super().area()
        return face_area * self.length

    def what_am_i(self):
        return 'Cube'

    def family_tree(self):
        return self.what_am_i() + ' child of ' + super(Cube, self).what_am_i()