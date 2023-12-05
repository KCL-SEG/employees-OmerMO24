"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name):
        self.name = name

    def get_pay(self):
        raise NotImplementedError("Subclasses must implement this method")

    def __str__(self):
        raise NotImplementedError("Subclasses must implement this method")


class SalaryEmployee(Employee): 
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary

    def get_pay(self):
        return self.monthly_salary

    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.monthly_salary}.\nTheir total pay is {self.get_pay()}."

class HourlyEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def get_pay(self):
        return self.hourly_rate * self.hours_worked

    def __str__(self):
        return f"{self.name} works on a contract of {self.hours_worked} hours at {self.hourly_rate}/hour.\nTheir total pay is {self.get_pay()}."

class SalaryWithContractCommission(SalaryEmployee): 
    def __init__(self, name, monthly_salary, commission, contracts):
        super().__init__(name, monthly_salary)
        self.commission = commission
        self.contracts = contracts

    def get_pay(self):
        return super().get_pay() + (self.commission * self.contracts)

    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.monthly_salary} and receives a commission for {self.contracts} contract(s) at {self.commission}/contract.\nTheir total pay is {self.get_pay()}."
    

class HourlyWithContractCommission(HourlyEmployee): 
    def __init__(self, name, hourly_rate, hours_worked, commission, contracts):
        super().__init__(name, hourly_rate, hours_worked)
        self.commission = commission
        self.contracts = contracts

    def get_pay(self):
        return super().get_pay() + self.commission * self.contracts

    def __str__(self):
        return f"{self.name} works on a contract of {self.hours_worked} hours at {self.hourly_rate}/hour and receives a commission for {self.contracts} contract(s) at {self.commission}/contract.\nTheir total pay is {self.get_pay()}."
    

class SalaryWithBonus(SalaryEmployee):
    def __init__(self, name, monthly_salary, bonus):
        super().__init__(name, monthly_salary)
        self.bonus = bonus

    def get_pay(self):
        return super().get_pay() + self.bonus

    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.monthly_salary} and receives a bonus commission of {self.bonus}.\nTheir total pay is {self.get_pay()}."
    

class HourlyWithBonus(HourlyEmployee):
    def __init__(self, name, hourly_rate, hours_worked, bonus):
        super().__init__(name, hourly_rate, hours_worked)
        self.bonus = bonus

    def get_pay(self):
        return super().get_pay() + self.bonus

    def __str__(self):
        return f"{self.name} works on a contract of {self.hours_worked} hours at {self.hourly_rate}/hour and receives a bonus commission of {self.bonus}.\nTheir total pay is {self.get_pay()}."

# Other classes remain unchanged




# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = SalaryEmployee('Billie', 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = HourlyEmployee('Charlie', 25, 100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = SalaryWithContractCommission('Renee', 3000, 200, 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan =  HourlyWithContractCommission('Jan', 25, 150, 220, 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = SalaryWithBonus('Robbie', 2000, 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = HourlyWithBonus('Ariel', 30, 120, 600)
