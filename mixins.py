"""
Multiple Inheritance is hard in Python.. Python community advices to limit its usage

Mixins solve the problem of code complexity in multiple inheritance.

Mixins are an alternative class design pattern that avoids both single-inheritance class fragmentation and multiple-inheritance diamond dependencies.

A mixin is a class that defines and implements a single, well-defined feature. Subclasses that inherit from the mixin inherit this feature—and nothing else.

Mixins:-
A mixin is an independent class that is pulled inside the inheritance heirarchy and can be used
anywhere because it doesn't care about its position in the inheritance heirarchy but provides one or more convenience methods..

Mixins provides convenience methods for the class but does not need to understand what it is used for
therefore removing dependency

Independence of mixins benefits the class structure in many ways because there is no name clash 
complexity anymore but the power of inheritance is still there.

A mixin is a special kind of multiple inheritance. There are two main situations where mixins are used:

You want to provide a lot of optional features for a class.
You want to use one particular feature in a lot of different classes.

Some examples to demonstrate the code sample.

For an example of number one, consider werkzeug's request and response system. I can make a plain old request object by saying:

from werkzeug import BaseRequest

class Request(BaseRequest):
    pass

Now If I want to add accept header support, I would make that.....

from werkzeug import BaseRequest, AcceptMixin

class Request(AcceptMixin, BaseRequest):
    pass


If I wanted to make a request object that supports accept headers, etags, authentication, and user agent support, I could do this

from werkzeug import BaseRequest, AcceptMixin, ETagRequestMixin, UserAgentMixin, AuthenticationMixin

class Request(AcceptMixin, ETagRequestMixin, UserAgentMixin, AuthenticationMixin, BaseRequest):
    pass

"""

class SurfaceAreaMixin:
    def surface_area(self):
        surface_area = 0
        for surface in self.surfaces:
            surface_area += surface.area(self)

        return surface_area

class Cube(Square, SurfaceAreaMixin):
    def __init__(self, length):
        super().__init__(length)
        self.surfaces = [Square, Square, Square, Square, Square, Square]

class RightPyramid(Square, Triangle, SurfaceAreaMixin):
    def __init__(self, base, slant_height):
        self.base = base
        self.slant_height = slant_height
        self.height = slant_height
        self.length = base
        self.width = base

        self.surfaces = [Square, Triangle, Triangle, Triangle, Triangle]