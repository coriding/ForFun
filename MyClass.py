class Employee:
    def __init__(self, first, last, pay, company):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@' + company + '.com'

emp1 = Employee("Mike", "Wizowski", 200000, "Wizowski")
emp1 = Employee("Steve", "Wonder", 2000000, "stevie")

print(emp1.first, emp1.last, ' Email:', emp1.email)

# this is a test

# second change

