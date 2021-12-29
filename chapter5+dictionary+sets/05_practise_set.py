# Problem :1
# myDict={
#     "Dabba":"Bos",
#     "aba":"father",
#     "tiddi":"saba",
#     "chaurail":"sadaf",
#     "shamo":"laraib"
# }
# print("The Options are :",myDict.keys())
# a=input("Enter the Urdu word\n")
# # print("The meaning of your word is :",myDict[a])
# print("The meaning of your word is :",myDict.get(a)) #it will not throws an error even no elment found in dictionary

# Problem :2
# num1=int(input("Enter the Num 1 \n"))
# num2=int(input("Enter the Num 2 \n"))
# num3=int(input("Enter the Num 3 \n"))
# num4=int(input("Enter the Num 4 \n"))
# num5=int(input("Enter the Num 5 \n"))
# num6=int(input("Enter the Num 6 \n"))
# num7=int(input("Enter the Num 7 \n"))
# num8=int(input("Enter the Num 8 \n"))
# set={num1,num2,num3,num4,num5,num6,num7,num8}
# print(set)


# USe ctr+alt+arrow keys to rotate the screen

# problem:3  this set will take the same value but differnt type
from os import pardir


s={18,"18",18.0}
print(s)

#problem :4
# what will be the length of this set
# the length of set will be 2 because it will take the float and int same value as one value
# s={20,20.0,"20"}
# print(len(s))


# problem:5
favLang={}
a=input("Enter your favourite language asif: \n")
b=input("Enter your favourite language tidd: \n")
c=input("Enter your favourite language Shabbir: \n")
d=input("Enter your favourite language Haris: \n")
favLang["asif"]=a
favLang["tiddi"]=b
favLang["tiddi"]=c
favLang['Haris']=d
print(favLang)

#problem6 if we do the same key in above progrma what will happen
# second vale will overide the first same key ,keys should be unique

# problem:7 in above problem 5 if values of two keys are same then no change will done because the value can be same but keys should be unique 

# problem :8
set={4,3,2,6,[4,6,7,7]} #can we change this set ?
# NO we cannot change set values or list inside the set is also strictly not allow
