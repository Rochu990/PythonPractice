# source https://www.youtube.com/watch?v=RSl87lqOXDE&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=4

class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.empoyees = []
        else:
            self.empoyees = employees

    def add_emp(self, emp):
        if emp not in self.empoyees:
            self.empoyees.append(emp)

    def remove_emp(self, emp):
        if emp in self.empoyees:
            self.empoyees.remove(emp)

    def print_emps(self):
        for emp in self.empoyees:
            print('-->', emp.fullname())


dev_1 = Developer('Corey', 'Schafer', 50000, 'Python' )
dev_2 = Developer('Test', 'Employee', 60000, "Java" )

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

print(isinstance(dev_1, Manager))