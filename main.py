#OPP

# Polymorphism Format
class Employee:
    def __init__(self, emp_id, emp_name, emp_department, emp_job_title, emp_salary, emp_location):
        # __init__ Holds A Set Of Attribute Like (id, name, salary, ,)
        self.id = emp_id
        self.name = emp_name
        self.department = emp_department
        self.job_title = emp_job_title
        self.__salary = emp_salary
        self.location = emp_location

    # And We Can Create Functions That Serve The Attribute

    def set_salary(self, new_salary):
        self.__salary = new_salary # Function To Modify Salary

    def get_salary(self):
        return self.__salary # To Use On if Condition Line 34 & Print Line 40

    def tax_salary(self):
        tax_amount = self.__salary * 0.10   # Calculate The Tax = 10% TAX
        return tax_amount

    def net_salary(self):
        net_salary = self.__salary - self.tax_salary()  # Calculate The Salary After The TAX
        return net_salary

    def display_info(self):
        print(f"Employee ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Job Title: {self.job_title}")
        # Permission
        if self.get_salary() >= 10000:
            print(f"Salary: None")
            print(f"Tax: None")
            print(f"Salary: None")
        # Calculate TAX
        else:
            print(f"Salary: {self.get_salary()} LE")      # salary before tax
            print(f"Tax: {self.tax_salary()} LE")         # salary tax value
            print(f"Net.Salary: {self.net_salary()} LE")  # salary after tax
        print(f"Location: {self.location}")


# Employees Info
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

# Polymorphism Format (Child)
class Manager(Employee):
    def __init__(self, manag_id, emp_id, emp_name, emp_department,
                 emp_job_title, emp_salary, emp_location, emp_chart):
        super().__init__(emp_id, emp_name, emp_department,
                         emp_job_title, emp_salary, emp_location)
        self.organization_chart = emp_chart
        self.manag_id = manag_id

    def display_info(self):
        print(f"Manag ID: {self.manag_id}")
        super().display_info()
        print(f"Organization Chart: {self.organization_chart}")


# Manger Info
manag1 = Manager(1, 7, 'Mostafa',
                'Operation', 'Operation Manager',
                20000, 'Administration', f"\nID: {emp1.id} - Name: {emp1.name}")

manag2 = Manager(2, 8, 'Yasser',
                'Finances', 'Financial Manager',
                18000, 'Administration', f"\nID: {emp3.id} - Name: {emp3.name}\n"
                                         f"ID: {emp4.id} - Name: {emp4.name}")

manag3 = Manager(3, 9, 'Essam',
                'Inventory', 'Inventory Manger',
                15000, 'Administration', f"\nID: {emp2.id} - Name: {emp2.name}\n"
                                         f"ID: {emp5.id} - Name: {emp5.name}\n"
                                         f"ID: {emp6.id} - Name: {emp6.name}")


# U Can Add New Salary Here, But It Must Be Before (.Display_info)
# Or Make New (.display_info) One For First Version And One For Last Updated Version Under The (set_salary)


# First Ver Of Employees
emp4.display_info()

# Set New Salary For Employees
emp4.set_salary(6500)

# Last Updated Ver Of Employee (Show Info)
emp1.display_info()
print()
emp2.display_info()
print()
emp3.display_info()
print()
emp4.display_info()
print()
emp5.display_info()
print()
emp6.display_info()
print()

# Managers Print Info
manag1.display_info()
print()
manag2.display_info()
print()
manag3.display_info()
print()