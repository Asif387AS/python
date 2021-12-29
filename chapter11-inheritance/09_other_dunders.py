class Number:
    def __init__(self,num):
        self.num=num
    def __add__(self,num2):
        print("let's add")
        return self.num+num2.num
    def __mul__(self,num2):
        print("let's multiply")
        return self.num*num2.num
    def __str__(self):
        return f"Decimal Number is {self.num}"
    def __len__(self):
        return 4
n=Number(3)
print(n)
print(len(n))