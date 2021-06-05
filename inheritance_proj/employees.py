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