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

    def get_salary(self):
            return self.__salary

    def tax_salary(self):
        tax_amount = self.__salary * 0.10   # calculate the tax = 10% TAX
        return tax_amount

    def net_salary(self):
        net_salary = self.__salary - self.tax_salary()  # calculate the salary after the tax
        return net_salary

    def display_info(self):
        print(f"Employee ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Jop Title: {self.jop_title}")
        #TAX And Permission
        if self.get_salary() >= 10000:
            print(f"Salary: None")
            print(f"Tax: None")
            print(f"Salary: None")
        else:
            print(f"Salary: {self.get_salary()} LE")
            print(f"Tax: {self.tax_salary()} LE")
            print(f"Net.Salary: {self.net_salary()} LE")
        print(f"Location: {self.location}\n")




emp1 = Employee(1, 'Hussein',
                'Operation', 'Operation Dev',
                12000, 'Administration')

emp2 = Employee(2, 'Mahmoud',
                'Inventory' , 'Store Keeper',
                5500, 'Branch')

emp3 = Employee(3, 'Ahmed',
                'Accounts', 'Accountant',
                10000 ,'Administration')

emp4 = Employee(4, 'Tamer',
                'Sales', 'Sales Representative',
                6000 ,'Branch')

emp5 = Employee(5, 'Mohamed',
                'Purchases', 'Purchasing Representative',
                6000 ,'Branch')

emp6 = Employee(6, 'Momen',
                'HR', 'Buffet Worker',
                4000 ,'Branch')

emp1.display_info()
emp2.display_info()
emp3.display_info()
emp4.display_info()
emp5.display_info()
emp6.display_info()