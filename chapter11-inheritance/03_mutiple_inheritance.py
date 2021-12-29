# Multiple inheritance:sigle derives class from two base class 
class Employee:
    company="visa"
    eCode=120
class Freelancer:
    company="Fiverr"
    level=0
    def getLevel(self):
        print(f"The level of the Employee is {self.level+1}")
        # self.level=self.level+1
class Programmer(Employee,Freelancer): #which class is written first his overided elements will print first : here first prioty to Employee
    name="asif"
p=Programmer()
print(p.getLevel())
print(p.company)
