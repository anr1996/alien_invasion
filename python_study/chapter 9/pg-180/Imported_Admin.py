


class Admin:
    def __init__(self, privileges, employees ):
        self.privileges = privileges
        self.employees = employees
        self.salary = 70_000


    def authority(self):
        print(f"Administrator has the current privileges:\n {self.privileges}\n")

    def people_employed(self):
        print(f"The Administrator has the current employees under them:\n {self.employees}\n")

    def annual_pay(self):
        print(f"Admins currently make ${self.salary} per year.\n")

startup_admin = Admin('add user, delete, user, suspend user, delete comments', "John, Tim, Jennifer")
startup_admin.authority()
startup_admin.people_employed()
startup_admin.annual_pay()


class Admins_lesser:
    def __init__(self, position, salary, name):
        self.position = position
        self.salary = salary
        self.name = name
        self.employee_status = "programmer"

    def job_title(self):
        print(f"Employees current job title is {self.position}.")

    def employee_pay(self):
        print(f"Employee's current salary is {self.salary}.")

    def employee_name(self):
        print(f"Employee name: {self.name}.")
    
    def get_descriptive_info(self):
        info = f"{self.position} {self.salary} {self.name}"
        return info

print("Information on our newest hire:")
my_employees = Admins_lesser('programmer', 50_000, 'John')
my_employees.employee_name()
my_employees.job_title()
my_employees.employee_pay()
print(f"\n")


class owner(Admins_lesser):
    def __init__(self, position, salary, name):
        """Initializing attributes of the parent class Admins_lesser"""
        super().__init__(position, salary, name)

new_employee = owner('owner', 3000_0000, 'Adrian')
print(new_employee.get_descriptive_info())

