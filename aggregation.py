"""
Aggregation also depicts a part-of or has-a relationship. The difference between aggregation and composition is:

In composition, the low-level component cannot exist independently of the high-level class. For example, in your project, Omixatlas has a Schema. 
The Schema cannot exist separately from the Omixatlas class. The parts cannot exist separately from the main class.

In aggregation, the low-level component can exist independently of the high-level class. For example, a airline and airplane; 
the airplane is a part of airline and can also exist independent of the airline.
"""

class Airline:
    def __init__(self, airline):
        self.airline = airline

class Airplane:
    def __init__(self):
        pass

# Creating an airplane instance
airplane = Airplane()

# Creating a Airline instance with the airplane instance
airline = Airline(airplane)

# Airplane exists independently of Airline
print(airplane)
print(airline.airplane)
