# problem:2
# name=input("Enter your name")
# marks=int(input("Enter your marks"))
# phone=int(input("Enter your phone number"))

# template="Name is {}, marks are {} and phone number is {}"
# output=template.format(name,marks,phone)
# print(output)

#problem:3
# l=[str(i*4) for i in range(1,11)]
# print(l)
# verticalTable=" \n ".join(l)
# print(verticalTable)

#problem:4
# l=[4,5,6,7,8,9,10,15,18,20,30,34,60,75]
# a=filter(lambda a:a%5==0, l)
# print(list(a))

#problem:5
from functools import reduce
l=[4,5,6,7,8,24,4,5,6,7,8,9,9]
a=reduce(max,l)
print(a)
