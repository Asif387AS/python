class Employee:
    company="Google"

    def __init__(self,name,selery,subunit):
        self.name=name
        self.selery=selery
        self.subunit=subunit
        print("Employee is created")

    def getDetails(self):
        print(f"my name is {self.name},my salery is {self.selery} and i work on {self.subunit}")

    def quiin(self,love):
        print(f"{self.quiin1} is my {love}")
    @staticmethod  #if use static method no need of self argument
    def getData(signature):
        name="quiin" #class attributes
        print(f"Asif selery is 200K {signature}")

    @staticmethod
    def time():
        print("Now Time is 10:29 PM 9 Sep 2021")

        
Employee1=Employee("asif",434343,"Youtube")
Employee1.getDetails()