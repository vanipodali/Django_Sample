class Employee:
    def __init__(self, emp_id, name, age):
        self.emp_id = emp_id
        self.name = name
        self.age = age

            
Class Manager(Employee):
    def __init__(self, emp_id, name, age):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        for Employee1 in self.Employee:
            print(Employee1.emp_id, Employee1.name, Employee1.age)

obj1 = Employee(1, 'Vani', 23)
obj2 = Employee(2, 'Soni', 24)
Manager.Employee.append(obj1)
Manager.Employee.append(obj2)




