class Employees:
    """Employee class houses information on name and salary"""
    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary
        
        
    def give_raise(self, custom_raise = None):
        if custom_raise:
            self.annual_salary += custom_raise
        else:
            self.annual_salary += 5000


        
