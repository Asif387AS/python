class Person:
    company="Fiverr"
    def takeBreath(self):
        print("i am breating at person class")
class Employee(Person):
    def takeBreath(self):
        print("i am breating at Employee class")
class Programmer(Employee):
    def takeBreath(self):
        print("i am breating at Programmer class")

p=Person()
p.takeBreath()
e=Employee()
e.takeBreath()
pr=Programmer()
pr.takeBreath()