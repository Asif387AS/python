class Employee:
    company="Google"
    def getData(self):
        name="quiin" #class attributes
        print("Asif selery is 200K",self.company)
asif=Employee()
asif.company="facebook" #instance attributes
asif.getData()  #=Employee.getData(asif)
