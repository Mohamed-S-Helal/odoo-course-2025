class Person:
    counter = 0

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    @classmethod
    def get_count(cls):
        return cls.counter

    @staticmethod
    def say_hello():
        print("static method")

    def can_eat(self):
        print("yes can eat")

    def can_sleep(self):
        print("yes can sleep")

    def can_walk(self):
        print("yes can walk")

    def get_info(self):
        print(f"name: {self.name}, age: {self.age}, address: {self.address}")


class Employee(Person):
    def __init__(self, name, age, address, job, department):
        super().__init__(name, age, address)
        self.job = job
        self.department = department

    def get_info(self):
        print(f"{super().get_info()}, job: {self.job}, department: {self.department}")


ibrahim = Employee("ibrahim", 43, "64 eltahrer st, cairo, egypt", "accountant", "accounting")

ibrahim.get_info()


