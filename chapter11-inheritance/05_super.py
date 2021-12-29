class Person:
    company="Fiverr"
    def __init__(self):
        print("Person initializing....\n")
    def takeBreath(self):
        print("i am breating at person class")
class Employee(Person):
    def __init__(self):
        super().__init__()
        print("Employee initializing....\n") 
    def takeBreath(self):
        super().takeBreath() #it will say that plzz bro first run the takeBreath() of Person
        print("i am breating at Employee class")
class Programmer(Employee):
    def __init__(self):
          super().__init__()
          print("Programmer initializing....\n")
    def takeBreath(self):
        super().takeBreath() # it will say that plzz bro first run the takeBreath() of Employee
        print("i am breating at Programmer class")

# p=Person()
# p.takeBreath()
# e=Employee()
# e.takeBreath()
# pr=Programmer()
# pr.takeBreath()

p=Programmer()
# p.takeBreath()