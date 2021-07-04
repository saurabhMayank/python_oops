from abc import ABC, abstractmethod

# Employee class, see concepts.txt for further explanation
class Employee(ABC):
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.address = None
    
    @abstractmethod
    def calculate_payroll(self):
        pass

# Categories of employee, see concepts.txt for further explanation
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



# Types of employee, see concepts.txt for further explanation
class Manager(SalaryEmployee):
    def work(self, hours):
        print(f'{self.name} screams and yells for {hours} hours.')

class Secretary(SalaryEmployee):
    def work(self, hours):
        print(f'{self.name} spends {hours} doing office paper work.')

class SalesPerson(CommisionEmployee):   
    def work(self, hours):
        print(f'{self.name} spends {hours} on the phone.')



class TemporarySecretary(Secretary, HourlyEmployee):
    def __init__(self, id, name, hours_worked, hour_rate):
        HourlyEmployee.__init__(self, id, name, hours_worked, hour_rate)
    
    def calculate_payroll(self):
        return HourlyEmployee.calculate_payroll(self)

