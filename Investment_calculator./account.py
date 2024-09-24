from utils import *

class common_rates:
    def __init__(self, principal_amount, interest_rate, period_per_year, time_years):
        
         self.principal_amount = float(principal_amount)
         self.interest_rate = float(interest_rate)
         self.period_per_year = float(period_per_year)
         self.time_years = float(time_years)
         
    def simple_interest_rate(self):
        rate = self.principal_amount * self.interest_rate * self.time_years
        return rate
    
    def compound_interest_rate(self):
        rate = self.principal_amount * (1 + (self.interest_rate / self.period_per_year)) ** (self.period_per_year * self.time_years)
        return rate
    
    def annual_percentage_rate(self):
        rate = self.interest_rate * self.period_per_year
        return rate
        
    def annual_percentage_yield(self):
        rate = ((1 + (self.interest_rate / self.period_per_year)) ** self.period_per_year) - 1
        return rate
    
class loans(common_rates):
    """Different types of loans, some of which include common rates."""
    
    def __init__(self, principal_amount, interest_rate, period_per_year, time_years):
        super().__init__(principal_amount, interest_rate, period_per_year, time_years)
        self.payments = 0
        self.mortgage_balance = 0
        self.draw_period = 0
        self.credit_limit = 0
        
    def personal_loan(self):
        total_amount = self.principal_amount + common_rates.simple_interest_rate(self)
        return total_amount
    
    def amortization_equation(self):
        """equation used for auto loans and mortgages"""
        
        rate = self.interest_rate / MONTHS_PER_YEAR
        total_payments = self.time_years * MONTHS_PER_YEAR
        monthly_payment = (self.principal_amount * rate * ((1 + rate) ** total_payments)) / (((1 + rate) ** total_payments) - 1)
        return monthly_payment


    def home_equity(self, balance):
        self.mortgage_balance = balance
        equity = self.principal_amount - self.mortgage_balance
        return equity
    
    def equity_loan(self, payment_plan, total_borrowed):
        self.principal_amount = total_borrowed
        
        if payment_plan == "Monthly installments.":
            return self.amortization_equation()

        elif payment_plan == "Lump sum.":
            total_amount = self.principal_amount + self.simple_interest_rate()
            return total_amount
        
    
    def heloc_period(self, draw, total_credit_limit):
        self.draw_period = draw
        self.credit_limit = total_credit_limit
        
    def heloc_credit(self, amount_borrowed, total_days):
        interest = amount_borrowed * (self.interest_rate / 365) * (total_days / 365)
        self.principal_amount += amount_borrowed
        return interest
    
    
    
    
        
        