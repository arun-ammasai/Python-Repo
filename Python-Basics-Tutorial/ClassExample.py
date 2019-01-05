class Employee :
    def __init__(self,name,designation) :
        self.name = name
        self.designation = designation

    def sayHello(self) :
        print("Welcome to Python Course")

emp = Employee("Dennis John","Salesman")
print("Before :My Name is {} and working as a {}".format(emp.name,emp.designation))
emp.designation = "PA"
print("After : My Name is {} and working as a {}".format(emp.name,emp.designation))
#emp = Employee("Coulson","Manager")
#print("My Name is {} and working as a {}".format(emp.name,emp.designation))
emp.sayHello()
