class Employee:
    company="Google"
    def quiin(self,love):
        print(f"{self.quiin1} is my {love}")
    @staticmethod  #if use static method no need of self argument
    def getData(signature):
        name="quiin" #class attributes
        print(f"Asif selery is 200K {signature}")

    @staticmethod
    def time():
        print("Now Time is 10:29 PM 9 Sep 2021")

        
asif=Employee()
asif.quiin1='quiin'
asif.quiin("Love")

asif.company="facebook" #instance attributes
asif.getData("Thanks!")  #=Employee.getData(asif)
asif.time()
