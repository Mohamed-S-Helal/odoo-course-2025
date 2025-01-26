#print('hussein tarek')

#OPP

#new
class Employee:
    def __init__(self, emp_name, emp_salary):
        print('hello')
        self.name = emp_name
        self.__salary = emp_salary

emp1 = Employee('ahmed', 5000)
emp2 = Employee('hussein', 7000)
print(emp1.name)
print(emp2.name)