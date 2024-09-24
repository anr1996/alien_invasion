class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.annual_salary = 50_000

    def first_name(self):
        """employee's first name"""
        print(self.first)
        
    def last_name(self):
        """employee's last name"""
        print(self.last)

    def employee_current_pay(self):
        """"employee's salary"""
        print(f"${self.annual_salary}")

    def give_raise(self, employee_raise):
        """employee's raise"""
        self.annual_salary += employee_raise
        print(f"${employee_raise}")


    
    
    
    
