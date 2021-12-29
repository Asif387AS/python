#problem:1
# def readFile(filename):
#     try:
#         with open(filename,'r') as f:
#             print(f.read())
#     except FileNotFoundError as e:
#         print(f"Sorry! file {filename }not found ")
# readFile('1.txt')
# readFile('2.txt')
# readFile('3.txt')

# problem:2
# l=[1,2,3,4,5,6,7,8,9,10]
# for index,item in enumerate(l):
#     if index==4 or index==6 or index==8:
#         # print(index,item)
#         print(f"The {index+1}th element of list is {item}")

#problem:3
# num=int(input("Enter the number:"))

# table=[num*i for i in range(1,11)]
# print(table)

# for i in range(1,11):
#     print(num*i)

#problem:4
# a=int(input("Enter the first number:"))
# b=int(input("Enter the second number"))
# try:
#     c=a/b
#     print(c)
# except ZeroDivisionError as e:
#     print("Infinte")

# problem:5
num=int(input("Enter the number:"))

table=[num*i for i in range(1,11)]
print(str(table))

with open('table.txt','a') as f:
    print(f.write(str(table)))
    print('\n')
