from employee import Employee

company_employees = Employee('john', 'ash')

print("Employee's first name: ")
company_employees.first_name()
print("\n")

print("Employee's last name: ")
company_employees.last_name()
print("\n")

print("Employee's current salary of the year 2022:")
company_employees.employee_current_pay()
print("\n")

print("Employee's raise for the year 2023:")
company_employees.give_raise(10_000)
print("\n")

print("Employee's new salary for the year 2023:")
company_employees.employee_current_pay()