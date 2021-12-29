# class C2dVec:
#     def __init__(self,i,j):
#         self.icap=i
#         self.jcap=j
#     def __str__(self):
#         return f"{self.icap}i+{self.jcap}j"
# class C3dVec(C2dVec):
#     def __init__(self,i,j,k):
#         super().__init__(i,j)
#         self.kcap=k
#     def __str__(self):
#         return f"{self.icap}i+{self.jcap}j+{self.kcap}k"
# v2d=C2dVec(3,5)
# v3d=C3dVec(4,6,7)
# print(v2d)
# print(v3d)


# class Animal:
#     animalType="Mammal"
# class Pets:
#     color:"white"
# class Dog:
#     @staticmethod
#     def Bark():
#         print("Bow Bow!")
# d=Dog()
# d.Bark()

# Problem#3
# class Employee:
#     Salary=1000
#     increment=1.5
#     @property
#     def salaryAfterIncrement(self):
#         return self.Salary*self.increment
#     @salaryAfterIncrement.setter
#     def salaryAfterIncrement(self,sai):
#         self.increment=sai/self.Salary
# e=Employee()
# print(e.salaryAfterIncrement)
# e.salaryAfterIncrement=2000
# print(e.increment)

#problem:4
# class Complex:
#     def __init__(self,r,i):
#         self.real=r
#         self.imaginary=i
#     def __add__(self,c):
#         return Complex(self.real+c.real,self.imaginary+c.imaginary)
#     def __mul__(self,c):
#         mulReal=self.real*c.real-self.imaginary*c.imaginary
#         mulImg=self.real*c.imaginary + self.imaginary*c.real
#         # return Complex(self.real+c.real,self.imaginary+c.imaginary)
#         return Complex(mulReal,mulImg)
#     def __str__(self):
        #   if self.imaginary<0:
#              return f"{self.real}-{-self.imaginary}i"
#           return f"{self.real}-{-self.imaginary}i"
# c1=Complex(4,6)
# c2=Complex(3,6)
# print(c1+c2)
# print(c1*c2)
