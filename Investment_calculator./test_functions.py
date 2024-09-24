import unittest

from account import *

class common_rates_TestCase(unittest.TestCase):
    """Tests for common_rates class."""
    
    def test_simple_interest_rate(self):
        """check calculation"""
        
        check_rate = common_rates(10000, 0.04, 1, 10).simple_interest_rate()
        self.assertEqual(check_rate, 4000)

        check_rate_1 = common_rates(1534.5, 0.075, 1, 35).simple_interest_rate()
        self.assertAlmostEqual(check_rate_1, 4028.0625)
        
        check_rate_2 = common_rates(30000, 0.09, 1, 50).simple_interest_rate()
        self.assertEqual(check_rate_2, 135000)
        
        
    def test_compound_interest_rate(self):
        """check calculation"""
        
        check_rate = common_rates(0.50, 0.01, 1, 1).compound_interest_rate()
        self.assertAlmostEqual(check_rate, 0.505)

        check_rate_1 = common_rates(5000.57, 0.06, 4, 10).compound_interest_rate()
        self.assertAlmostEqual(check_rate_1, 9071.126034, places=5)
        
        check_rate_2 = common_rates(99999573, 0.0357, 2, 60).compound_interest_rate()
        self.assertAlmostEqual(check_rate_2, 835702810.2, places=1)
    
    
    def test_annual_percentage_rate(self):
        """check calculation"""
        
        check_rate = common_rates(0.7, 0.02, 1, 1).annual_percentage_rate()
        self.assertAlmostEqual(check_rate, 0.02, places=2)
        
        check_rate_1 = common_rates(0.7, 0.055, 2, 1).annual_percentage_rate()
        self.assertAlmostEqual(check_rate_1, 0.11)
        
        check_rate_2 = common_rates(0.7, 0.09937, 4, 1).annual_percentage_rate()
        self.assertAlmostEqual(check_rate_2, 0.39748)
        
    def test_annual_percentage_yield(self):
        """check calculation"""
        
        check_rate = common_rates(0.50, 0.01, 1, 1).annual_percentage_yield()
        self.assertAlmostEqual(check_rate, 0.01)
        
        check_rate_1 = common_rates(5000, 0.055, 2, 5).annual_percentage_yield()
        self.assertAlmostEqual(check_rate_1, 0.05575625, places=8)
        
        check_rate_2 = common_rates(150250.70, 0.09, 4, 50).annual_percentage_yield()
        self.assertAlmostEqual(check_rate_2, 0.09308331, places=7)
        
        
class loans_TestCase(unittest.TestCase):
    """tests for loans class"""
    
    def test_personal_loan(self):
        """check calculation"""
        
        check_total = loans(10, 0.01, 1, 5).personal_loan()
        self.assertAlmostEqual(check_total, 10.5, places=2)
        
        check_total = loans(10000, 0.04, 1, 10).personal_loan()
        self.assertEqual(check_total, 14000)
        
        check_total = loans(32850701.5, 0.09, 1, 50).personal_loan()
        self.assertAlmostEqual(check_total + 0.05, 180678858.3, places=1) # approximation off by roughly 0.05, verified answer with calculator.
        
    def test_amortization_equation(self):
        """check calculation"""
        
        check_total = loans(300533.50, 0.01, 0, 10).amortization_equation()
        self.assertAlmostEqual(check_total, 2632.797321, places=2)
        
        check_total_1 = loans(700000, 0.04, 0, 30).amortization_equation()
        self.assertAlmostEqual(check_total_1, 3341.907125, places=2)
        
        check_total_2 = loans(1500000, 0.09, 0, 15).amortization_equation()
        self.assertAlmostEqual(check_total_2, 15213.99876, places=2)
        
    def test_equity_equation(self):
        """check calculation"""
        
        check_total = loans(300533, 0.01, 0, 10).home_equity(10000)
        self.assertEqual(check_total, 290533)
        
        check_total = loans(5000345.50, 0.05, 0, 20).home_equity(100000)
        self.assertEqual(check_total, 4900345.5)
        
        check_total = loans(959934599, 0.09, 0, 30).home_equity(1009900)
        self.assertEqual(check_total, 958924699)
    
    def test_equity_loan(self):
        """Check calculation monthly installments."""
        
        check_total = loans(700000, 0.01, 0, 5).equity_loan("Monthly installments.", 50000)
        self.assertAlmostEqual(check_total, 854.6873723, places=2)
        
        check_total_1 = loans(1122750.70, 0.05, 0, 20).equity_loan("Monthly installments.", 250397.52)
        self.assertAlmostEqual(check_total_1, 1652.51281, places=2)
        
        check_total_2 = loans(2250000, 0.09, 0, 50).equity_loan("Monthly installments.", 400250)
        self.assertAlmostEqual(check_total_2, 3036.174983, places=2)
        
        """Check calculation Lump sum."""
        
        check_total_3 = loans(700000, 0.01, 0, 1).equity_loan("Lump sum.", 50000)
        self.assertAlmostEqual(check_total_3, 50500.0, places=1)
        
        check_total_4 = loans(1122750.70, 0.05, 0, 2).equity_loan("Lump sum.", 100000)
        self.assertEqual(check_total_4, 110000)
        
        check_total_5 = loans(2250000, 0.09, 0, 5).equity_loan("Lump sum.", 250350)
        self.assertAlmostEqual(check_total_5, 363007.50, places=2)
        
if __name__ == '__main__':
    unittest.main()