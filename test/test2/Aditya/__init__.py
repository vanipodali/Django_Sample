class Employee:

    def __init__(self, emp_id, name, age):
        self.emp_id = emp_id
        self.name = name
        self.age = age

    @property
    def email(self):
        return self.name+'@'+'email.com'

    @staticmethod
    def double_the_age(self):
        return self.age1 * 2

    @classmethod
    def create_an_object(cls, emp_id, name, age):
        return Employee.__init__(emp_id, name, age)

obj1 = Employee(1, 'Vani', 12)
obj2 = Employee(2, 'Soni', 13)

print(Employee. email)
print(Employee.double_the_age)
print(Employee.create_an_object)

