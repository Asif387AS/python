#problem:1
# def max(num1,num2,num3):
#     if(num1>num2):
#         if(num1>num3):
#             return num1
#         else:
#             return num3
#     else:
#         if(num2>num3):
#             return num2
#         else:
#             return num3
# m=max(4,65,77)
# print("The max number is :",m)
# print("The max number is :"+str(m)) #same type is joined using + operator

#problem:2  cellsisus to farh
# def farh(cel):
#     return (cel*(9/5))+32

# c=22
# f=farh(c)
# print("The fahrenheit tempurature is:" +str(f))

#problem :# print in one line
# print("Hello" ,end="")
# print("How" ,end="")
# print("are" ,end="")
# print("you?" ,end="")

#problem:4
# def sum(n):
#     if n==-1 or n==0:
#         return -1
#     return sum(n-1)+n
     
# s=sum(5)
# print(s)

#problem:5
# n=4
# for i in range(n):
#     print("*" * (n-i))

#problem:6 convert m to cms

#proble:7
#strip function removes the extra spaces in string
# def remove_and_split(string,word):
#     newStr=string.replace(word,"")
#     # newStr=string.delete(word)
#     return newStr.strip()
# s=remove_and_split("   Asif is a good boy    ","Asif")
# print(s)

#problem:8

def multiplication(n):
    i=1
    while i<=10:
        # print("The multiplication of number is :" ,n*i)
         i=i+1
    return (f"Multiplication table of {n} is {n*i}")
m=multiplication(10)
print(m)