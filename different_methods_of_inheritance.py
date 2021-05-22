"""
Objective of this Python file
1. Single Inheritance => (A -> B)

2. Heirarchical Inheritance => (A -> B, A -> C, A -> D)

3. Multiple Inheritance => ((A, B, C) -> D)

4. Multilevel Inheritance => (A-> B -> C -> D)

To read and know about all the different types of inheritance 
See which of them can be coded in Python..
Showcase with examples

IMP Points :-
1) This is because every class you create in Python implicitly derives from object. You could be more explicit and write class MyClass(object):, but it’s redundant and unnecessary.

2) Exception class which throw errors are an exception to the above statement. They don't implcitly derive from an object class

3) For class which depict exception, we should derive it from Exception classes..
class MyError(Exception):
    pass

4) The isinstance() function is used to determine if an object is of a specific type
for example :-
class Baby(Person):
    # Baby code here
isinstance(baby, Person) is True



Overriding:-
1) Overriding the attributes and methods of parent class in the child class.

For example :-
class Person:
    DESCRIPTION = "general person"

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def speak(self):
        print("I am {} and my age is {}".format(self.name, self.age))

class Baby(Person):
    DESCRIPTION = "baby"

    def speak(self):
        print("ba ba ba ba")

Here we have overrided the description attribute of Person class in baby class.
Also we have overrided the speak method of Person class in the baby class.


"""



"""
Depicting Inheritance with an example :-
Modeling an HR system:-
1)The HR system needs to process payroll for the company’s employees, 
2)But there are different types of employees depending on how their payroll is calculated
"""

class PayrollSystem:
    def calculate_payroll(self, employees):
        print('Calculating Payroll')
        print('===================')
        for employee in employees:
            print(f'Payroll for: {employee.id} - {employee.name}')
            print(f'- Check amount: {employee.calculate_payroll()}')
            print('')


#Base class for all the employees
class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

# Calculates Salaries of each employee
class SalaryEmployee(Employee):
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary
