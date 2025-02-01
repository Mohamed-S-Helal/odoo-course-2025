# OOP

class Employee:
    def __init__(self, emp_name, emp_salary):
        self.name = emp_name
        self.__salary = emp_salary

    def get_salary(self):
        if not self.__salary > 50000:
            return self.__salary
        else:
            return None

    def set_salary(self, new_salary):
        self.__salary = new_salary

    def display_info(self):
        print(f"Name: {self.name}, Salary: {self.__salary}")

# emp1 = Employee('ahmed', 70000)
# emp2 = Employee('mohamed', 7000)
#
# emp1.set_salary(5000)
#
# emp1.display_info()


class Manager(Employee):
    def __init__(self, emp_name, emp_salary, emp_department):
        super().__init__(emp_name, emp_salary)
        self.department = emp_department

    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")





class cars :
    def __init__(self, car_name, car_type):
        self.carname = car_name
        self.cartype = car_type

class cars(Employee):
    def __init__(self, emp_name, emp_salary, carype, carame):
        super().__init__(emp_name, emp_salary)
        self.carty = carype
        self.carnam = carame
    def display_info(self):
        super().display_info()
        print(f"cars: {self.carty}, cars:{self.carnam}")

m1 = cars('mahmed', 70000, 'toyota', "manga")
m1.display_info()
