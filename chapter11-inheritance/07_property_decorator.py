class Employee:
    salary=6000
    bonus=200
    @property
    def totalSalary(self):
        return self.salary+self.bonus
    @totalSalary.setter
    def tatolSalary(self,val):
        self.bonus=val-self.salary
e=Employee()
print(e.totalSalary)
e.tatolSalary=500
print(e.salary)
print(e.bonus)
# print(e.val)