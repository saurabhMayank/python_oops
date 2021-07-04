# import employees
# import hr
# import productivity
# from contacts import Address

# manager = employees.Manager(1, 'John Smith', 1500)
# manager.address = Address(
#     '121 Admin Road',
#     'Concord',
#     'NH',
#     '03301'
# )
# secretary = employees.Secretary(2, 'Jone Doe', 1200)
# sales_person = employees.SalesPerson(3, 'kevin becon', 1000, 250)
# temporary_secretary = employees.TemporarySecretary(5, 'Robin Williams', 40, 9)

# employees = [
#     manager,
#     secretary,
#     sales_person,
#     temporary_secretary
# ]

# productivity_system = productivity.ProductivitySystem()
# productivity_system.track(employees, 40)


# # Here if we pass generic_employee obj into the calculate payroll_method
# # of payroll system then it will break as generic_employee does not have calculate_payroll func
# # method... Employee Class should be a abstract class which should only be inherited.. Not Instantiated
# # generic_employee = hr.Employee(4," Jaden Smith")

# payroll_system = hr.PayrollSystem()
# payroll_system.calculate_payroll(employees)

from hr import PayrollSystem
from productivity import ProductivitySystem
from employees import EmployeeDatabase

productivity_system = ProductivitySystem()
payroll_system = PayrollSystem()
employee_database = EmployeeDatabase()
employees = employee_database.employees
productivity_system.track(employees, 40)
payroll_system.calculate_payroll(employees)