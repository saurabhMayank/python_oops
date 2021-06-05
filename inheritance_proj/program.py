import employees

salary_employee = employees.SalaryEmployee(1, 'John Smith', 1500)
hourly_employee = employees.HourlyEmployee(1, 'John Doe', 40, 15)
commission_employee = employees.CommisionEmployee(3, 'kevin becon', 1000, 250)

# Here if we pass generic_employee obj into the calculate payroll_method
# of payroll system then it will break as generic_employee does not have calculate_payroll func
# method... Employee Class should be a abstract class which should only be inherited.. Not Instantiated
# generic_employee = hr.Employee(4," Jaden Smith")

payroll_system = hr.PayrollSystem()
payroll_system.calculate_payroll([salary_employee, hourly_employee, commission_employee])
