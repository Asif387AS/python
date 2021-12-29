# from _typeshed import Self


class Employee:
    compnay="Google"
    def showDetails(self):
        print(f"The employee is working at {self.compnay}")
class Programmer(Employee):
    language="python"
    compnay="Youtube"
    def getLanguage(self):
        print(f"The langauge of programmer is {self.language}")
    def showDetails(self):
           print(f"The Programmer is working at {self.compnay}")
e=Employee()
p=Programmer()
# print(e.compnay)
# e.showDetails()
# print(p.compnay)
# p.showDetails()
p.showDetails()
print(p.compnay)