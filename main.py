#print('hussein tarek')

#OPP

#new
class Employee:
    def __init__(self, emp_id, emp_name, emp_department, emp_jop_title, emp_salary, emp_location):
        self.id = emp_id
        self.name = emp_name
        self.department = emp_department
        self.jop_title = emp_jop_title
        self.__salary = emp_salary
        self.location = emp_location

    def display_info(self):
        print(f"Employee ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Jop Title: {self.jop_title}")
        print(f"Salary: {self.__salary} LE")
        print(f"Location: {self.location}\n")


emp1 = Employee(1, 'Hussein',
                'Accounts', 'Operation Dev',
                6500, 'Administration')

emp2 = Employee(2, 'Mahmoud',
                'Inventory' , 'Store Keeper',
                4500, 'Branch')

emp3 = Employee(3, 'Ahmed',
                'Accounts', 'Accountant',
                10000 ,'Administration')

emp4 = Employee(4, 'Tamer',
                'Sales', 'Sales Representative',
                4500 ,'Branch')

emp5 = Employee(5, 'Mohamed',
                'Purchases', 'Purchasing Representative',
                5500 ,'Branch')

emp6 = Employee(6, 'Momen',
                'HR', 'Buffet Worker',
                3000 ,'Branch')

emp1.display_info()
emp2.display_info()
emp3.display_info()
emp4.display_info()
emp5.display_info()
emp6.display_info()