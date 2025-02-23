import unittest
from main import Employees

class TestEmployeeClass(unittest.TestCase):
    """Test Employee class to verify annual salary methods"""
    
    def setUp(self):
        self.my_employee = Employees('Adrian', 'Rich', 100000)
     
     
    def test_default_salary(self):
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.annual_salary, 105000)
        
    def test_custom_salary(self):
        self.my_employee.give_raise(600)
        self.assertEqual(self.my_employee.annual_salary, 100600)
        
        
if __name__ == '__main__':
    unittest.main()