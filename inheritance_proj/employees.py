from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    @abstractmethod
    def calculate_payroll(self):
        pass

class SalaryEmployee(Employee):
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary
    
    def calculate_payroll(self):
        return self.weekly_salary

class HourlyEmployee(Employee):
    def __init__(self, id, name, hour_worked, hour_rate):
        super().__init__(id, name)
        self.hour_worked = hour_worked
        self.hour_rate =  hour_rate
    
    def calculate_payroll(self):
        return self.hour_worked * self.hour_rate

class CommisionEmployee(SalaryEmployee):
    def __init__(self, id, name, weekly_salary, commision):
        super().__init__(id, name, weekly_salary)
        self.commision = commision
    
    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        variable = self.commision
        return fixed+variable

"""
 We’re not going to declare an .__init__() method here. This will mean that the Manager class will inherit the .__init__() method from SalaryEmployee implicitly, meaning that when we create a Manager object, we’ll need to pass in an id, a name, and a weekly_salary...
"""

class Manager(SalaryEmployee):
    def work(self, hours):
        print(f'{self.name} screams and yells for {hours} hours.')

class Secretary(SalaryEmployee):
    def work(self, hours):
        print(f'{self.name} spends {hours} doing office paper work.')

class SalesPerson(CommisionEmployee):
    def work(self, hours):
        print(f'{self.name} spends {hours} on the phone.')

# __mro__ => TemporarySecretary, Secretary, SalaryEmployee, Hourly Employee, Employee, Object
# Every class has its own mro.

# In multiple Inheritance mro is from left to right.
# First child class is executed and then the parent class is executed depending on 
# left to right order in the inheritance chain

#  The TemporarySecretary class performs the role of a Secretary 
#  in the context of the   ProductivitySystem, but for payroll purposes, 
#  it is an HourlyEmployee.

"""
Diamond Problem
The diagram shows the diamond problem with the current class design. TemporarySecretary uses multiple inheritance to derive from two classes that ultimately also derive from Employee. This causes two paths to reach the Employee base class, which is something you want to avoid in your designs.

The diamond problem appears when you’re using multiple inheritance and deriving from two classes that have a common base class. This can cause the wrong version of a method to be called.

As you’ve seen, Python provides a way to force the right method to be invoked, and analyzing the MRO can help you understand the problem.

Still, when you run into the diamond problem, it’s better to re-think the design. You will now make some changes to leverage multiple inheritance, avoiding the diamond problem.

"""


class TemporarySecretary(Secretary, HourlyEmployee):
    def __init__(self, id, name, hours_worked, hour_rate):
        HourlyEmployee.__init__(self, id, name, hours_worked, hour_rate)
    
    def calculate_payroll(self):
        return HourlyEmployee.calculate_payroll(self)