# num=int(input("Enter the number\n"))
# for i in range(1,11):
#     # print(str(num)+"X"+str(i)+"="+str(num*i))
#     # print((num)+"X"+(i)+"="+(num*i))  #it will throw an error
#     print(f"{num}X{i}={num*i}") #this is f string 

#problem :2
# l1=['Asif','Saba','Tiddi','Sadaf']
# for name in l1:
#     if name.startswith("S"):
#         print("Hello "+name)

#problem:3
# num=int(input("Enter the number\n"))
# i=1
# while i<=10:
#      print(f"{num}X{i}={num*i}") #this is f string 
#      i=i+1

#problem:10
num=int(input("Enter the number\n"))
i=10
while i>0:
     print(f"{num}X{i}={num*i}") #this is f string 
     i=i-1


# problem :4
# num=int(input("Enter the Number:\n"))
# prime=True
# for i in range(2,num):
#     if(num%i==0):
#      prime=False
#     break
# if prime:
#     print("This number is prime")
# else:
#     print("This number is not prime")

#problem:5
# num=int(input("Enter the Number:\n"))
# sum=0
# for i in range(1,11):
#     sum=sum+i

# print(sum)
#    OR 
# num=int(input("Enter the Number:\n"))
# sum=0
# for i in range(0,num+1):
#     sum=sum+i
# print(f"The sum of {num} is {sum}")

#problem:6
# factorial=1
# num=int(input("Enter the Number:\n"))
# for i in range(1,num+1):
#     factorial=factorial*i
# print(f"The factorial of {num} is {factorial}")

#problem:7
# num=int(input("Enter the Number:\n"))
# for i in range(num):
#     print("*" * (i+1))

#problem:8
# num=int(input("Enter the Number:\n"))
# for i in range(num):
#     print(" "* (num-i-1),end="")
#     print("*"* (2*i+1),end="")
#     print(" "* (num-i-1),)