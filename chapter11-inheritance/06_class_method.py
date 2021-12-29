class Employee:
    company="Fiverr"
    salary="100"
    location="FSD"
    def changeSalary(self,sal):
        self.__class__.salary=sal
    # @classmethod
    # def changeSalary(cls,sal):
    #     cls.salary=sal
e=Employee()
print(e.salary)
e.changeSalary(555)
print(e.salary)
print(Employee.salary)