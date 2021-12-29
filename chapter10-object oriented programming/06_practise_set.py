#problem:1
# class Programmer:
#     campany:'Microsoft'
#     def __init__(self,name,product):
#         self.name=name
#         self.product=product
#     def geInfo(self):
#         print(f"The name of programmer is {self.name} and its product is {self.product}")
# Asif=Programmer('asif','Facebook')
# Shabbir=Programmer('shabbir','google')
# Asif.geInfo()
# Shabbir.geInfo()

#problem:2
# class Calculator:
#     def __init__(self,num):
#         self.num=num
#     def square(self):
#         print(f"The Square of {self.num} is {self.num**2}")
#     def squareRoot(self):
#         print(f"The squareRoot of {self.num} is {self.num**.5}")
        
#     def cube(self):
#         print(f"The cube  of {self.num} is {self.num**3}")
# Cal=Calculator(3)
# Cal.square()
# Cal.squareRoot()
# Cal.cube()
        
#problem:3
# class Sample:
#     a="asif"
# Obj=Sample()
# Obj.a="QUiin"
# # Sample.a="Quiin"
# print(Sample.a)
# print(Obj.a)

#problem:4
# class greet:
#     @staticmethod
#     def greeting():
#         print("**************Hello Welcome to the web developing life*******")
# gr=greet()
# gr.greeting()

#problem:5
class Train:
    def __init__(self,name,fare,seats):
        self.name=name
        self.fare=fare
        self.seats=seats
    def getInfo(self):
        print(f"The name of the train is {self.name} and seats in the train are {self.seats}")
    def fareInfo(self):
        print(f"The fare of the train ticke is {self.fare}")
    def tickeBook(self):
        if(self.seats>0):
            print(f"Your ticket has been bocked! Your seat no is {self.seats}")
            self.seats=self.seats-1
        else:
            print(f"Sorry! train is full try for takkal")
    def cancelTicket(self):
        if(self.name==""):
            print("Ticket is cancelled")


intercity=Train("",3000,300)
intercity.getInfo()
intercity.fareInfo()
intercity.tickeBook()
intercity.tickeBook()
intercity.cancelTicket()
