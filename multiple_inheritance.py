"""
Multiple Inheritance in Python

Inheriting from multiple classes
A(B,C)

1) In case of multiple inheritance if many parents are there for a child
2) Then when calling super().a(). Python will first look for method `a` in first parent 
i.e. B and then look for the method `a` in the second parent parent i.e. C..
"""

# Intermediate code snippet
# Focus on the method resolution order

class A:
    def __init__(self):
        print('A')
        super().__init__()

class B(A):
    def __init__(self):
        print('B')
        super().__init__()

class X:
    def __init__(self):
        print('X')
        super().__init__()

class Forward(B, X):
    def __init__(self):
        print('Forward')
        super().__init__()

class Backward(X, B):
    def __init__(self):
        print('Backward')
        super().__init__()

"""
Forward.__mro__ => Forward -> B -> A (A's init class object which does not print so)
-> X
Forward, B,A,X (This will be printed)
This is because X is next parent in the order so once B's __mro__ is complete
X's __mro__ will start
"""

"""
But we have a problem here.. Which is that
Attributes in the child class have different name then parent class
So calling inside of child's class init and passing the variables 
with different names can cause bugs because these variables in child means 
different things and this will mean different in parent..
Example :-
Right Pyramid is inheriting from square and traingle

Right Pyramid mein Attributes -> Base and Slant height
But Square mein attributes -> length and breadth hain

"""
"""
Combining mro and keyword args (**kwargs) feature in Python


"""



#Final Code Snippet

class Rectangle:
    def __init__(self, length, width, **kwargs):
        self.length = length
        self.width = width
        super().__init__(**kwargs)

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

class Square(Rectangle):
    def __init__(self, length, **kwargs):
        super().__init__(length=length, width=length, **kwargs)

class Triangle:
    def __init__(self, base, height, **kwargs):
        self.base = base
        self.height = height
        super().__init__(**kwargs)

    def tri_area(self):
        return 0.5 * self.base * self.height

class RightPyramid(Square, Triangle):
    def __init__(self, base, slant_height, **kwargs):
        self.base = base
        self.slant_height = slant_height
        kwargs["height"] = slant_height
        kwargs["length"] = base
        super().__init__(base=base, **kwargs)

    def area(self):
        base_area = super().area()
        perimeter = super().perimeter()
        return 0.5 * perimeter * self.slant_height + base_area

    def area_2(self):
        base_area = super().area()
        triangle_area = super().tri_area()
        return triangle_area * 4 + base_area
